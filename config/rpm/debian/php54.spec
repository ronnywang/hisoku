Name:		php54
Version:	5.5.6
Release:	1%{?dist}
Summary:	PHP54

Group:		Hisoku
License:	No
URL:		http://hisoku.ronny.tw/
Source0:	php-5.5.6.tar.gz
# http://www.php.net/get/php-5.5.6.tar.gz/from/a/mirror
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
%description


%prep
%setup -q -n php-5.5.6

%build
%configure --enable-fpm --with-config-file-scan-dir=/etc/php.d/ --with-config-file-path=/etc --enable-mysqlnd --with-mysql --with-pgsql --with-pdo-mysql --with-pdo-pgsql --with-mysqli --with-zlib --with-gettext --enable-pcntl --with-curl --with-openssl --with-gd
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
/.channels/.alias/pear.txt
/.channels/.alias/pecl.txt
/.channels/.alias/phpdocs.txt
/.channels/__uri.reg
/.channels/doc.php.net.reg
/.channels/pear.php.net.reg
/.channels/pecl.php.net.reg
/.depdb
/.depdblock
/.filemap
/.lock
/etc/pear.conf
/usr/bin/pear
/usr/bin/peardev
/usr/bin/pecl
/usr/bin/phar
/usr/bin/phar.phar
/usr/bin/php
/usr/bin/php-cgi
/usr/bin/php-config
/usr/bin/phpize
/usr/include/php/TSRM/TSRM.h
/usr/include/php/TSRM/readdir.h
/usr/include/php/TSRM/tsrm_config.h
/usr/include/php/TSRM/tsrm_config.w32.h
/usr/include/php/TSRM/tsrm_config_common.h
/usr/include/php/TSRM/tsrm_nw.h
/usr/include/php/TSRM/tsrm_strtok_r.h
/usr/include/php/TSRM/tsrm_virtual_cwd.h
/usr/include/php/TSRM/tsrm_win32.h
/usr/include/php/Zend/zend.h
/usr/include/php/Zend/zend_API.h
/usr/include/php/Zend/zend_alloc.h
/usr/include/php/Zend/zend_build.h
/usr/include/php/Zend/zend_builtin_functions.h
/usr/include/php/Zend/zend_closures.h
/usr/include/php/Zend/zend_compile.h
/usr/include/php/Zend/zend_config.h
/usr/include/php/Zend/zend_config.nw.h
/usr/include/php/Zend/zend_config.w32.h
/usr/include/php/Zend/zend_constants.h
/usr/include/php/Zend/zend_dtrace.h
/usr/include/php/Zend/zend_dynamic_array.h
/usr/include/php/Zend/zend_errors.h
/usr/include/php/Zend/zend_exceptions.h
/usr/include/php/Zend/zend_execute.h
/usr/include/php/Zend/zend_extensions.h
/usr/include/php/Zend/zend_float.h
/usr/include/php/Zend/zend_gc.h
/usr/include/php/Zend/zend_globals.h
/usr/include/php/Zend/zend_globals_macros.h
/usr/include/php/Zend/zend_hash.h
/usr/include/php/Zend/zend_highlight.h
/usr/include/php/Zend/zend_indent.h
/usr/include/php/Zend/zend_ini.h
/usr/include/php/Zend/zend_ini_parser.h
/usr/include/php/Zend/zend_ini_scanner.h
/usr/include/php/Zend/zend_ini_scanner_defs.h
/usr/include/php/Zend/zend_interfaces.h
/usr/include/php/Zend/zend_istdiostream.h
/usr/include/php/Zend/zend_iterators.h
/usr/include/php/Zend/zend_language_parser.h
/usr/include/php/Zend/zend_language_scanner.h
/usr/include/php/Zend/zend_language_scanner_defs.h
/usr/include/php/Zend/zend_list.h
/usr/include/php/Zend/zend_llist.h
/usr/include/php/Zend/zend_modules.h
/usr/include/php/Zend/zend_multibyte.h
/usr/include/php/Zend/zend_multiply.h
/usr/include/php/Zend/zend_object_handlers.h
/usr/include/php/Zend/zend_objects.h
/usr/include/php/Zend/zend_objects_API.h
/usr/include/php/Zend/zend_operators.h
/usr/include/php/Zend/zend_ptr_stack.h
/usr/include/php/Zend/zend_qsort.h
/usr/include/php/Zend/zend_signal.h
/usr/include/php/Zend/zend_stack.h
/usr/include/php/Zend/zend_static_allocator.h
/usr/include/php/Zend/zend_stream.h
/usr/include/php/Zend/zend_string.h
/usr/include/php/Zend/zend_strtod.h
/usr/include/php/Zend/zend_ts_hash.h
/usr/include/php/Zend/zend_types.h
/usr/include/php/Zend/zend_variables.h
/usr/include/php/Zend/zend_vm.h
/usr/include/php/Zend/zend_vm_def.h
/usr/include/php/Zend/zend_vm_execute.h
/usr/include/php/Zend/zend_vm_opcodes.h
/usr/include/php/ext/date/lib/timelib.h
/usr/include/php/ext/date/lib/timelib_config.h
/usr/include/php/ext/date/lib/timelib_structs.h
/usr/include/php/ext/date/php_date.h
/usr/include/php/ext/dom/xml_common.h
/usr/include/php/ext/ereg/php_ereg.h
/usr/include/php/ext/ereg/php_regex.h
/usr/include/php/ext/ereg/regex/cclass.h
/usr/include/php/ext/ereg/regex/cname.h
/usr/include/php/ext/ereg/regex/regex.h
/usr/include/php/ext/ereg/regex/regex2.h
/usr/include/php/ext/ereg/regex/utils.h
/usr/include/php/ext/filter/php_filter.h
/usr/include/php/ext/hash/php_hash.h
/usr/include/php/ext/hash/php_hash_adler32.h
/usr/include/php/ext/hash/php_hash_crc32.h
/usr/include/php/ext/hash/php_hash_fnv.h
/usr/include/php/ext/hash/php_hash_gost.h
/usr/include/php/ext/hash/php_hash_haval.h
/usr/include/php/ext/hash/php_hash_joaat.h
/usr/include/php/ext/hash/php_hash_md.h
/usr/include/php/ext/hash/php_hash_ripemd.h
/usr/include/php/ext/hash/php_hash_sha.h
/usr/include/php/ext/hash/php_hash_snefru.h
/usr/include/php/ext/hash/php_hash_tiger.h
/usr/include/php/ext/hash/php_hash_types.h
/usr/include/php/ext/hash/php_hash_whirlpool.h
/usr/include/php/ext/iconv/php_have_bsd_iconv.h
/usr/include/php/ext/iconv/php_have_glibc_iconv.h
/usr/include/php/ext/iconv/php_have_ibm_iconv.h
/usr/include/php/ext/iconv/php_have_iconv.h
/usr/include/php/ext/iconv/php_have_libiconv.h
/usr/include/php/ext/iconv/php_iconv.h
/usr/include/php/ext/iconv/php_iconv_aliased_libiconv.h
/usr/include/php/ext/iconv/php_iconv_supports_errno.h
/usr/include/php/ext/iconv/php_php_iconv_h_path.h
/usr/include/php/ext/iconv/php_php_iconv_impl.h
/usr/include/php/ext/json/php_json.h
/usr/include/php/ext/libxml/php_libxml.h
/usr/include/php/ext/pcre/pcrelib/config.h
/usr/include/php/ext/pcre/pcrelib/pcre.h
/usr/include/php/ext/pcre/pcrelib/pcre_internal.h
/usr/include/php/ext/pcre/pcrelib/pcreposix.h
/usr/include/php/ext/pcre/pcrelib/ucp.h
/usr/include/php/ext/pcre/php_pcre.h
/usr/include/php/ext/pdo/php_pdo.h
/usr/include/php/ext/pdo/php_pdo_driver.h
/usr/include/php/ext/session/mod_files.h
/usr/include/php/ext/session/mod_user.h
/usr/include/php/ext/session/php_session.h
/usr/include/php/ext/spl/php_spl.h
/usr/include/php/ext/spl/spl_array.h
/usr/include/php/ext/spl/spl_directory.h
/usr/include/php/ext/spl/spl_dllist.h
/usr/include/php/ext/spl/spl_engine.h
/usr/include/php/ext/spl/spl_exceptions.h
/usr/include/php/ext/spl/spl_fixedarray.h
/usr/include/php/ext/spl/spl_functions.h
/usr/include/php/ext/spl/spl_heap.h
/usr/include/php/ext/spl/spl_iterators.h
/usr/include/php/ext/spl/spl_observer.h
/usr/include/php/ext/sqlite3/libsqlite/sqlite3.h
/usr/include/php/ext/standard/base64.h
/usr/include/php/ext/standard/basic_functions.h
/usr/include/php/ext/standard/crc32.h
/usr/include/php/ext/standard/credits.h
/usr/include/php/ext/standard/credits_ext.h
/usr/include/php/ext/standard/credits_sapi.h
/usr/include/php/ext/standard/crypt_blowfish.h
/usr/include/php/ext/standard/crypt_freesec.h
/usr/include/php/ext/standard/css.h
/usr/include/php/ext/standard/cyr_convert.h
/usr/include/php/ext/standard/datetime.h
/usr/include/php/ext/standard/dl.h
/usr/include/php/ext/standard/exec.h
/usr/include/php/ext/standard/file.h
/usr/include/php/ext/standard/flock_compat.h
/usr/include/php/ext/standard/fsock.h
/usr/include/php/ext/standard/head.h
/usr/include/php/ext/standard/html.h
/usr/include/php/ext/standard/html_tables.h
/usr/include/php/ext/standard/info.h
/usr/include/php/ext/standard/md5.h
/usr/include/php/ext/standard/microtime.h
/usr/include/php/ext/standard/pack.h
/usr/include/php/ext/standard/pageinfo.h
/usr/include/php/ext/standard/php_array.h
/usr/include/php/ext/standard/php_assert.h
/usr/include/php/ext/standard/php_browscap.h
/usr/include/php/ext/standard/php_crypt.h
/usr/include/php/ext/standard/php_crypt_r.h
/usr/include/php/ext/standard/php_dir.h
/usr/include/php/ext/standard/php_dns.h
/usr/include/php/ext/standard/php_ext_syslog.h
/usr/include/php/ext/standard/php_filestat.h
/usr/include/php/ext/standard/php_fopen_wrappers.h
/usr/include/php/ext/standard/php_ftok.h
/usr/include/php/ext/standard/php_http.h
/usr/include/php/ext/standard/php_image.h
/usr/include/php/ext/standard/php_incomplete_class.h
/usr/include/php/ext/standard/php_iptc.h
/usr/include/php/ext/standard/php_lcg.h
/usr/include/php/ext/standard/php_link.h
/usr/include/php/ext/standard/php_mail.h
/usr/include/php/ext/standard/php_math.h
/usr/include/php/ext/standard/php_metaphone.h
/usr/include/php/ext/standard/php_rand.h
/usr/include/php/ext/standard/php_smart_str.h
/usr/include/php/ext/standard/php_smart_str_public.h
/usr/include/php/ext/standard/php_standard.h
/usr/include/php/ext/standard/php_string.h
/usr/include/php/ext/standard/php_type.h
/usr/include/php/ext/standard/php_uuencode.h
/usr/include/php/ext/standard/php_var.h
/usr/include/php/ext/standard/php_versioning.h
/usr/include/php/ext/standard/proc_open.h
/usr/include/php/ext/standard/quot_print.h
/usr/include/php/ext/standard/scanf.h
/usr/include/php/ext/standard/sha1.h
/usr/include/php/ext/standard/streamsfuncs.h
/usr/include/php/ext/standard/uniqid.h
/usr/include/php/ext/standard/url.h
/usr/include/php/ext/standard/url_scanner_ex.h
/usr/include/php/ext/standard/winver.h
/usr/include/php/ext/xml/expat_compat.h
/usr/include/php/ext/xml/php_xml.h
/usr/include/php/main/SAPI.h
/usr/include/php/main/build-defs.h
/usr/include/php/main/fopen_wrappers.h
/usr/include/php/main/logos.h
/usr/include/php/main/php.h
/usr/include/php/main/php_compat.h
/usr/include/php/main/php_config.h
/usr/include/php/main/php_content_types.h
/usr/include/php/main/php_getopt.h
/usr/include/php/main/php_globals.h
/usr/include/php/main/php_ini.h
/usr/include/php/main/php_logos.h
/usr/include/php/main/php_main.h
/usr/include/php/main/php_memory_streams.h
/usr/include/php/main/php_network.h
/usr/include/php/main/php_open_temporary_file.h
/usr/include/php/main/php_output.h
/usr/include/php/main/php_reentrancy.h
/usr/include/php/main/php_scandir.h
/usr/include/php/main/php_streams.h
/usr/include/php/main/php_syslog.h
/usr/include/php/main/php_ticks.h
/usr/include/php/main/php_variables.h
/usr/include/php/main/php_version.h
/usr/include/php/main/rfc1867.h
/usr/include/php/main/snprintf.h
/usr/include/php/main/spprintf.h
/usr/include/php/main/streams/php_stream_context.h
/usr/include/php/main/streams/php_stream_filter_api.h
/usr/include/php/main/streams/php_stream_glob_wrapper.h
/usr/include/php/main/streams/php_stream_mmap.h
/usr/include/php/main/streams/php_stream_plain_wrapper.h
/usr/include/php/main/streams/php_stream_transport.h
/usr/include/php/main/streams/php_stream_userspace.h
/usr/include/php/main/streams/php_streams_int.h
/usr/include/php/main/win32_internal_function_disabled.h
/usr/include/php/main/win95nt.h
/usr/include/php/sapi/cli/cli.h
/usr/lib64/build/Makefile.global
/usr/lib64/build/acinclude.m4
/usr/lib64/build/config.guess
/usr/lib64/build/config.sub
/usr/lib64/build/libtool.m4
/usr/lib64/build/ltmain.sh
/usr/lib64/build/mkdep.awk
/usr/lib64/build/phpize.m4
/usr/lib64/build/run-tests.php
/usr/lib64/build/scan_makefile_in.awk
/usr/lib64/build/shtool
/usr/lib64/php/.channels/.alias/pear.txt
/usr/lib64/php/.channels/.alias/pecl.txt
/usr/lib64/php/.channels/.alias/phpdocs.txt
/usr/lib64/php/.channels/__uri.reg
/usr/lib64/php/.channels/doc.php.net.reg
/usr/lib64/php/.channels/pear.php.net.reg
/usr/lib64/php/.channels/pecl.php.net.reg
/usr/lib64/php/.depdb
/usr/lib64/php/.depdblock
/usr/lib64/php/.filemap
/usr/lib64/php/.lock
/usr/lib64/php/.registry/archive_tar.reg
/usr/lib64/php/.registry/console_getopt.reg
/usr/lib64/php/.registry/pear.reg
/usr/lib64/php/.registry/structures_graph.reg
/usr/lib64/php/.registry/xml_util.reg
/usr/lib64/php/Archive/Tar.php
/usr/lib64/php/Console/Getopt.php
/usr/lib64/php/OS/Guess.php
/usr/lib64/php/PEAR.php
/usr/lib64/php/PEAR/Autoloader.php
/usr/lib64/php/PEAR/Builder.php
/usr/lib64/php/PEAR/ChannelFile.php
/usr/lib64/php/PEAR/ChannelFile/Parser.php
/usr/lib64/php/PEAR/Command.php
/usr/lib64/php/PEAR/Command/Auth.php
/usr/lib64/php/PEAR/Command/Auth.xml
/usr/lib64/php/PEAR/Command/Build.php
/usr/lib64/php/PEAR/Command/Build.xml
/usr/lib64/php/PEAR/Command/Channels.php
/usr/lib64/php/PEAR/Command/Channels.xml
/usr/lib64/php/PEAR/Command/Common.php
/usr/lib64/php/PEAR/Command/Config.php
/usr/lib64/php/PEAR/Command/Config.xml
/usr/lib64/php/PEAR/Command/Install.php
/usr/lib64/php/PEAR/Command/Install.xml
/usr/lib64/php/PEAR/Command/Mirror.php
/usr/lib64/php/PEAR/Command/Mirror.xml
/usr/lib64/php/PEAR/Command/Package.php
/usr/lib64/php/PEAR/Command/Package.xml
/usr/lib64/php/PEAR/Command/Pickle.php
/usr/lib64/php/PEAR/Command/Pickle.xml
/usr/lib64/php/PEAR/Command/Registry.php
/usr/lib64/php/PEAR/Command/Registry.xml
/usr/lib64/php/PEAR/Command/Remote.php
/usr/lib64/php/PEAR/Command/Remote.xml
/usr/lib64/php/PEAR/Command/Test.php
/usr/lib64/php/PEAR/Command/Test.xml
/usr/lib64/php/PEAR/Common.php
/usr/lib64/php/PEAR/Config.php
/usr/lib64/php/PEAR/Dependency2.php
/usr/lib64/php/PEAR/DependencyDB.php
/usr/lib64/php/PEAR/Downloader.php
/usr/lib64/php/PEAR/Downloader/Package.php
/usr/lib64/php/PEAR/ErrorStack.php
/usr/lib64/php/PEAR/Exception.php
/usr/lib64/php/PEAR/FixPHP5PEARWarnings.php
/usr/lib64/php/PEAR/Frontend.php
/usr/lib64/php/PEAR/Frontend/CLI.php
/usr/lib64/php/PEAR/Installer.php
/usr/lib64/php/PEAR/Installer/Role.php
/usr/lib64/php/PEAR/Installer/Role/Cfg.php
/usr/lib64/php/PEAR/Installer/Role/Cfg.xml
/usr/lib64/php/PEAR/Installer/Role/Common.php
/usr/lib64/php/PEAR/Installer/Role/Data.php
/usr/lib64/php/PEAR/Installer/Role/Data.xml
/usr/lib64/php/PEAR/Installer/Role/Doc.php
/usr/lib64/php/PEAR/Installer/Role/Doc.xml
/usr/lib64/php/PEAR/Installer/Role/Ext.php
/usr/lib64/php/PEAR/Installer/Role/Ext.xml
/usr/lib64/php/PEAR/Installer/Role/Php.php
/usr/lib64/php/PEAR/Installer/Role/Php.xml
/usr/lib64/php/PEAR/Installer/Role/Script.php
/usr/lib64/php/PEAR/Installer/Role/Script.xml
/usr/lib64/php/PEAR/Installer/Role/Src.php
/usr/lib64/php/PEAR/Installer/Role/Src.xml
/usr/lib64/php/PEAR/Installer/Role/Test.php
/usr/lib64/php/PEAR/Installer/Role/Test.xml
/usr/lib64/php/PEAR/Installer/Role/Www.php
/usr/lib64/php/PEAR/Installer/Role/Www.xml
/usr/lib64/php/PEAR/PackageFile.php
/usr/lib64/php/PEAR/PackageFile/Generator/v1.php
/usr/lib64/php/PEAR/PackageFile/Generator/v2.php
/usr/lib64/php/PEAR/PackageFile/Parser/v1.php
/usr/lib64/php/PEAR/PackageFile/Parser/v2.php
/usr/lib64/php/PEAR/PackageFile/v1.php
/usr/lib64/php/PEAR/PackageFile/v2.php
/usr/lib64/php/PEAR/PackageFile/v2/Validator.php
/usr/lib64/php/PEAR/PackageFile/v2/rw.php
/usr/lib64/php/PEAR/Packager.php
/usr/lib64/php/PEAR/REST.php
/usr/lib64/php/PEAR/REST/10.php
/usr/lib64/php/PEAR/REST/11.php
/usr/lib64/php/PEAR/REST/13.php
/usr/lib64/php/PEAR/Registry.php
/usr/lib64/php/PEAR/RunTest.php
/usr/lib64/php/PEAR/Task/Common.php
/usr/lib64/php/PEAR/Task/Postinstallscript.php
/usr/lib64/php/PEAR/Task/Postinstallscript/rw.php
/usr/lib64/php/PEAR/Task/Replace.php
/usr/lib64/php/PEAR/Task/Replace/rw.php
/usr/lib64/php/PEAR/Task/Unixeol.php
/usr/lib64/php/PEAR/Task/Unixeol/rw.php
/usr/lib64/php/PEAR/Task/Windowseol.php
/usr/lib64/php/PEAR/Task/Windowseol/rw.php
/usr/lib64/php/PEAR/Validate.php
/usr/lib64/php/PEAR/Validator/PECL.php
/usr/lib64/php/PEAR/XMLParser.php
/usr/lib64/php/PEAR5.php
/usr/lib64/php/Structures/Graph.php
/usr/lib64/php/Structures/Graph/Manipulator/AcyclicTest.php
/usr/lib64/php/Structures/Graph/Manipulator/TopologicalSorter.php
/usr/lib64/php/Structures/Graph/Node.php
/usr/lib64/php/System.php
/usr/lib64/php/XML/Util.php
/usr/lib64/php/data/PEAR/package.dtd
/usr/lib64/php/data/PEAR/template.spec
/usr/lib64/php/data/Structures_Graph/LICENSE
/usr/lib64/php/doc/Archive_Tar/docs/Archive_Tar.txt
/usr/lib64/php/doc/PEAR/INSTALL
/usr/lib64/php/doc/PEAR/LICENSE
/usr/lib64/php/doc/PEAR/README
/usr/lib64/php/doc/Structures_Graph/docs/generate.sh
/usr/lib64/php/doc/Structures_Graph/docs/html/Structures_Graph/Structures_Graph.html
/usr/lib64/php/doc/Structures_Graph/docs/html/Structures_Graph/Structures_Graph_Manipulator_AcyclicTest.html
/usr/lib64/php/doc/Structures_Graph/docs/html/Structures_Graph/Structures_Graph_Manipulator_TopologicalSorter.html
/usr/lib64/php/doc/Structures_Graph/docs/html/Structures_Graph/Structures_Graph_Node.html
/usr/lib64/php/doc/Structures_Graph/docs/html/Structures_Graph/_Structures_Graph_Manipulator_AcyclicTest_php.html
/usr/lib64/php/doc/Structures_Graph/docs/html/Structures_Graph/_Structures_Graph_Manipulator_TopologicalSorter_php.html
/usr/lib64/php/doc/Structures_Graph/docs/html/Structures_Graph/_Structures_Graph_Node_php.html
/usr/lib64/php/doc/Structures_Graph/docs/html/Structures_Graph/_Structures_Graph_php.html
/usr/lib64/php/doc/Structures_Graph/docs/html/Structures_Graph/tutorial_Structures_Graph.pkg.html
/usr/lib64/php/doc/Structures_Graph/docs/html/classtrees_Structures_Graph.html
/usr/lib64/php/doc/Structures_Graph/docs/html/elementindex.html
/usr/lib64/php/doc/Structures_Graph/docs/html/elementindex_Structures_Graph.html
/usr/lib64/php/doc/Structures_Graph/docs/html/errors.html
/usr/lib64/php/doc/Structures_Graph/docs/html/index.html
/usr/lib64/php/doc/Structures_Graph/docs/html/li_Structures_Graph.html
/usr/lib64/php/doc/Structures_Graph/docs/html/media/banner.css
/usr/lib64/php/doc/Structures_Graph/docs/html/media/stylesheet.css
/usr/lib64/php/doc/Structures_Graph/docs/html/packages.html
/usr/lib64/php/doc/Structures_Graph/docs/html/todolist.html
/usr/lib64/php/doc/Structures_Graph/docs/tutorials/Structures_Graph/Structures_Graph.pkg
/usr/lib64/php/doc/XML_Util/examples/example.php
/usr/lib64/php/doc/XML_Util/examples/example2.php
/usr/lib64/php/pearcmd.php
/usr/lib64/php/peclcmd.php
/usr/lib64/php/test/Structures_Graph/tests/AllTests.php
/usr/lib64/php/test/Structures_Graph/tests/testCase/BasicGraph.php
/usr/lib64/php/test/XML_Util/tests/AllTests.php
/usr/lib64/php/test/XML_Util/tests/testBasic_apiVersion.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_attributesToString.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_collapseEmptyTags.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_createCDataSection.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_createComment.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_createEndElement.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_createStartElement.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_createTag.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_createTagFromArray.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_getDocTypeDeclaration.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_getXmlDeclaration.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_isValidName.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_raiseError.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_replaceEntities.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_reverseEntities.phpt
/usr/lib64/php/test/XML_Util/tests/testBasic_splitQualifiedName.phpt
/usr/lib64/php/test/XML_Util/tests/testBug_4950.phpt
/usr/lib64/php/test/XML_Util/tests/testBug_5392.phpt
/usr/share/man/man1/php-config.1.gz
/usr/share/man/man1/php.1.gz
/usr/share/man/man1/phpize.1.gz
/etc/php-fpm.conf.default
/usr/sbin/php-fpm
/usr/share/fpm/status.html
/usr/share/man/man8/php-fpm.8.gz
/usr/include/php/ext/mysqli/mysqli_mysqlnd.h
/usr/include/php/ext/mysqli/php_mysqli_structs.h
/usr/include/php/ext/mysqlnd/config-win.h
/usr/include/php/ext/mysqlnd/mysqlnd.h
/usr/include/php/ext/mysqlnd/mysqlnd_alloc.h
/usr/include/php/ext/mysqlnd/mysqlnd_block_alloc.h
/usr/include/php/ext/mysqlnd/mysqlnd_charset.h
/usr/include/php/ext/mysqlnd/mysqlnd_debug.h
/usr/include/php/ext/mysqlnd/mysqlnd_enum_n_def.h
/usr/include/php/ext/mysqlnd/mysqlnd_ext_plugin.h
/usr/include/php/ext/mysqlnd/mysqlnd_libmysql_compat.h
/usr/include/php/ext/mysqlnd/mysqlnd_net.h
/usr/include/php/ext/mysqlnd/mysqlnd_portability.h
/usr/include/php/ext/mysqlnd/mysqlnd_priv.h
/usr/include/php/ext/mysqlnd/mysqlnd_result.h
/usr/include/php/ext/mysqlnd/mysqlnd_result_meta.h
/usr/include/php/ext/mysqlnd/mysqlnd_reverse_api.h
/usr/include/php/ext/mysqlnd/mysqlnd_statistics.h
/usr/include/php/ext/mysqlnd/mysqlnd_structs.h
/usr/include/php/ext/mysqlnd/mysqlnd_wireprotocol.h
/usr/include/php/ext/mysqlnd/php_mysqlnd.h
/usr/include/php/ext/mysqlnd/php_mysqlnd_config.h
/usr/include/php/ext/gd/gdcache.h
/usr/include/php/ext/gd/libgd/gd.h
/usr/include/php/ext/gd/libgd/gd_compat.h
/usr/include/php/ext/gd/libgd/gd_intern.h
/usr/include/php/ext/gd/libgd/gd_io.h
/usr/include/php/ext/gd/libgd/gdcache.h
/usr/include/php/ext/gd/libgd/gdfontg.h
/usr/include/php/ext/gd/libgd/gdfontl.h
/usr/include/php/ext/gd/libgd/gdfontmb.h
/usr/include/php/ext/gd/libgd/gdfonts.h
/usr/include/php/ext/gd/libgd/gdfontt.h
/usr/include/php/ext/gd/libgd/gdhelpers.h
/usr/include/php/ext/gd/libgd/jisx0208.h
/usr/include/php/ext/gd/libgd/wbmp.h
/usr/include/php/ext/gd/libgd/webpimg.h
/usr/include/php/ext/gd/php_gd.h

%changelog

