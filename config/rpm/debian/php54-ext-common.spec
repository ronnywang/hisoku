Name:		php54-ext-common
Version:	5.4.16
Release:	1%{?dist}
Summary:	php54-ext-common

Group:		Hisoku
License:	No
URL:		http://hisoku.ronny.tw/
Source0:	php-5.4.16.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:       autoconf
%description


%prep
%setup -q -n php-5.4.16


%build
for EXT in ctype fileinfo posix simplexml tokenizer xmlreader xmlwriter mbstring pdo_mysql zip; do
cd ext/${EXT}
phpize
%configure
make %{?_smp_mflags}
cd ../../
done


%install
rm -rf %{buildroot}
for EXT in ctype fileinfo posix simplexml tokenizer xmlreader xmlwriter mbstring pdo_mysql zip; do
cd ext/${EXT}
make install INSTALL_ROOT=%{buildroot}
cd ../../
done


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
/usr/lib64/extensions/no-debug-non-zts-20100525/ctype.so
/usr/lib64/extensions/no-debug-non-zts-20100525/fileinfo.so
/usr/lib64/extensions/no-debug-non-zts-20100525/posix.so
/usr/lib64/extensions/no-debug-non-zts-20100525/simplexml.so
/usr/lib64/extensions/no-debug-non-zts-20100525/tokenizer.so
/usr/lib64/extensions/no-debug-non-zts-20100525/xmlreader.so
/usr/lib64/extensions/no-debug-non-zts-20100525/xmlwriter.so
/usr/include/php/ext/mbstring/libmbfl/config.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/eaw_table.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfilter.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfilter_8bit.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfilter_pass.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfilter_wchar.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_allocators.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_consts.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_convert.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_defs.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_encoding.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_filter_output.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_ident.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_language.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_memory_device.h
/usr/include/php/ext/mbstring/libmbfl/mbfl/mbfl_string.h
/usr/include/php/ext/mbstring/mbstring.h
/usr/include/php/ext/mbstring/oniguruma/oniguruma.h
/usr/include/php/ext/mbstring/php_mbregex.h
/usr/include/php/ext/mbstring/php_onig_compat.h
/usr/lib64/extensions/no-debug-non-zts-20100525/mbstring.so
/usr/lib64/extensions/no-debug-non-zts-20100525/pdo_mysql.so
/usr/lib64/extensions/no-debug-non-zts-20100525/zip.so

%changelog

