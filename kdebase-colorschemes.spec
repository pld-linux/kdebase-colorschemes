Summary:	Collection of additional color schemes for KDE
Summary(pl):	Kolekcja dodatkowych schematów kolorów dla KDE
Name:		kdebase-colorschemes
Version:	050620
Release:	1
License:	Mixed (some are GPL, some LGPL, some BSD, but all opensource)
Group:		Themes
Source0:	%{name}.tar.bz2
# Source0-md5:	66d7224c7f3c0fd10d5f925bc4ce43a6
Requires:	kdebase-core
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of additional color schemes for KDE.

%description -l pl
Kolekcja dodatkowych schematów kolorów dla KDE.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes

%{__tar} xfj %{SOURCE0} -C $RPM_BUILD_ROOT%{_datadir}/apps/kdisplay/color-schemes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/apps/kdisplay/color-schemes
