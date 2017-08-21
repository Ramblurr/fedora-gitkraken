#
# spec file for package gitkraken
#
# Copyright (c) 2017 Casey Link <unnamedrambler@gmail.com>
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#
%global debug_package %{nil}

Name:           gitkraken
Version:        2.7.1
Release:        0
License:        Shareware
AutoReqProv:    no
Summary:        GUI for git
Url:            https://gitkraken.com/
Group:          IDE
Source0:        https://release.gitkraken.com/linux/gitkraken-amd64.tar.gz
Source1:        %{name}.svg
Source2:        LICENSE.gitkraken
BuildRequires:  desktop-file-utils
#BuildRequires:  hicolor-icon-theme
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64

%description
GitKraken makes Git commands and processes easy, fast, and intuitive.
Enjoy a visually appealing experience that requires fewer interactions,
allows for more fluid workflows, and provides total functionality.

%prep
%setup -q -n %{name}

%build

%install
install -Dpm 644 %{SOURCE2} ./
for file in content_shell.pak gitkraken icudtl.dat libffmpeg.so \
    libnode.so natives_blob.bin snapshot_blob.bin version
do
    install -Dpm 644 $file %{buildroot}/%{_libexecdir}/%{name}/$file
done
chmod +x %{buildroot}/%{_libexecdir}/%{name}/gitkraken
for dir in locales resources
do
    mv $dir %{buildroot}/%{_libexecdir}/%{name}/$dir
done

install -dm 755 %{buildroot}%{_bindir}
ln -s %{_libexecdir}/%{name}/gitkraken %{buildroot}/%{_bindir}/%{name}
install -Dpm 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

# Desktop file
install -dm 755 %{buildroot}%{_datadir}/applications
cat >"%buildroot%_datadir/applications/%name.desktop" << EOF
[Desktop Entry]
Encoding=UTF-8
Name=GitKraken
GenericName=Git Client
Comment=GUI for git.
Exec=%{name} %F
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;RevisionControl;
EOF
desktop-file-install \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop

#%post
#%desktop_database_post
#%icon_theme_cache_post

#%postun
#%desktop_database_postun
#%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc LICENSE.gitkraken LICENSE LICENSES.chromium.html
%_bindir/%name
%_libexecdir/%name
%_datadir/applications/%{name}.desktop
%_datadir/icons/hicolor/scalable/apps/%{name}.svg

%changelog

