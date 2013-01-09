<?php

class ProjectRow extends Pix_Table_Row
{
    public function getFirstDomain()
    {
        // TODO: add custom domain
        return $this->name . USER_DOMAIN;
    }

    public function getLoggerCategory()
    {
        return $this->name . '_' . hash_hmac('sha256', $this->name, getenv('LOG_SECRET'));
    }

    public function getEAVs()
    {
        return EAV::search(array('table' => 'Project', 'id' => $this->id));
    }

    /**
     * getWebNodes 取得現在 Project 有哪些 Web node, 如果沒有會自動產生
     *
     * @return array WebNode
     */
    public function getWebNodes()
    {
        // find current
        $nodes = WebNode::search(array(
            'project_id' => $this->id,
            'status' => WebNode::STATUS_WEBNODE,
            'commit' => $this->commit,
        ));

        // TODO: find STATUS_WEBPROCESSING

        if (count($nodes)) {
            return $nodes;
        }

        // TODO: check deploying

        $choosed_nodes = array();
        while (true) {
            $free_nodes_count = count(WebNode::search(array('project_id' => 0)));
            if (!$free_nodes_count) {
                // TODO; log it
                throw new Exception('No free nodes');
            }

            if (!$random_node = WebNode::search(array('project_id' => 0))->offset(rand(0, $free_nodes_count - 1))->first()) {
                continue;
            }

            $random_node->update(array(
                'project_id' => $this->id,
                'commit' => $this->commit,
                'status' => WebNode::STATUS_WEBPROCESSING,
            ));

            $node_id = $random_node->port - 20000;
            $ip = long2ip($random_node->ip);

            $session = ssh2_connect($ip, 22);
            ssh2_auth_pubkey_file($session, 'root', WEB_PUBLIC_KEYFILE, WEB_KEYFILE);
            ssh2_exec($session, "clone {$this->name} {$node_id}");

            $session = ssh2_connect($ip, 22);
            ssh2_auth_pubkey_file($session, 'root', WEB_PUBLIC_KEYFILE, WEB_KEYFILE);
            ssh2_exec($session, "restart-web {$this->name} {$node_id}");

            $random_node->update(array(
                'status' => WebNode::STATUS_WEBNODE,
            ));
    
            $choosed_nodes[] = $random_node;

            if (count($choosed_nodes) >= 1) {
                break;
            }
        }

        return $choosed_nodes;
    }
}

class Project extends Pix_Table
{
    public function init()
    {
        $this->_name = 'project';
        $this->_primary = 'id';
        $this->_rowClass = 'ProjectRow';
        $this->enableTableCache();

        $this->_columns['id'] = array('type' => 'int', 'auto_increment' => true);
        $this->_columns['name'] = array('type' => 'varchar', 'size' => 64);
        $this->_columns['commit'] = array('type' => 'char', 'size' => 32);
        $this->_columns['created_at'] = array('type' => 'int');
        $this->_columns['created_by'] = array('type' => 'int');

        $this->_indexes['name'] = array('type' => 'unique', 'columns' => array('name'));

        $this->_relations['members'] = array('rel' => 'has_many', 'type' => 'ProjectMember', 'foreign_key' => 'project_id');
        $this->_relations['custom_domains'] = array('rel' => 'has_many', 'type' => 'CustomDomain', 'foreign_key' => 'project_id');
        $this->_relations['variables'] = array('rel' => 'has_many', 'type' => 'ProjectVariable', 'foreign_key' => 'project_id');
        $this->_relations['webnodes'] = array('rel' => 'has_many', 'type' => 'WebNode', 'foreign_key' => 'project_id');
        $this->_relations['cronjobs'] = array('rel' => 'has_many', 'type' => 'CronJob', 'foreign_key' => 'project_id');

        $this->_hooks['eavs'] = array('get' => 'getEAVs');

        $this->addRowHelper('Pix_Table_Helper_EAV', array('getEAV', 'setEAV'));

    }

    public static function getRandomName()
    {
        $areas = array('taipei', 'taoyuan', 'hsinchu', 'yilan', 'hualien', 'miaoli', 'taichung', 'changhua', 'nantou', 'chiayi', 'yunlin', 'tainan', 'penghu', 'kaohiung', 'pingtung', 'kinmen', 'matsu', 'taitung');
        $first_names = array('An', 'Chang', 'Chao', 'Chen', 'Cheng', 'Chi', 'Chiang', 'Chien', 'Chin', 'Chou', 'Chu', 'Fan', 'Fang', 'Fei', 'Feng', 'Fu', 'Han', 'Hao', 'Ho', 'Hsi', 'Hsiao', 'Hsieh', 'Hsu', 'Hsueh', 'Hua', 'Huang', 'Jen', 'Kang', 'Ko', 'Ku', 'Kung', 'Lang', 'Lei', 'Li', 'Lien', 'Liu', 'Lo', 'Lu', 'Ma', 'Meng', 'Miao', 'Mu', 'Ni', 'Pai', 'Pan', 'Pao', 'Peng', 'Pi', 'Pien', 'Ping', 'Pu', 'Shen', 'Shih', 'Shui', 'Su', 'Sun', 'Tang', 'Tao', 'Teng', 'Tou', 'Tsao', 'Tsen', 'Tsou', 'Wang', 'Wei', 'Wu', 'Yang', 'Yen', 'Yin', 'Yu', 'Yuan', 'Yueh', 'Yun');

        for ($i = 0; $i < 10; $i ++) {
            $random = strtolower($areas[rand(0, count($areas) - 1)] . '-' . $first_names[rand(0, count($first_names) - 1)] . '-' . rand(100000, 1000000));

            if (!Project::find_by_name($random)) {
                break;
            }
        }

        if ($i > 5) {
            trigger_error("random {$i} times... too much times", E_USER_WARNING);
        }
        return $random;
    }
}
