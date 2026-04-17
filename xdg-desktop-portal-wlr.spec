Summary:	xdg-desktop-portal backend for wlroots
Name:		xdg-desktop-portal-wlr
Version:	0.8.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://github.com/emersion/xdg-desktop-portal-wlr/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	54a2380ad4316215da520f1cbd314fed
URL:		https://github.com/emersion/xdg-desktop-portal-wlr
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	inih-devel
BuildRequires:	libdrm-devel
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pipewire-devel >= 0.3.62
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	scdoc >= 1.9.7
BuildRequires:	systemd-devel
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.24
Requires:	pipewire-libs >= 0.3.62
Requires:	xdg-desktop-portal
Suggests:	grim
Suggests:	slurp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		filterout_cpp	-DNDEBUG

%description
xdg-desktop-portal backend for wlroots.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_user_post xdg-desktop-portal-wlr.service

%preun
%systemd_user_preun xdg-desktop-portal-wlr.service

%files
%defattr(644,root,root,755)
%doc CONTRIBUTING.md LICENSE README.md
%attr(755,root,root) %{_libexecdir}/xdg-desktop-portal-wlr
%{systemduserunitdir}/xdg-desktop-portal-wlr.service
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.wlr.service
%{_datadir}/xdg-desktop-portal/portals/wlr.portal
%{_mandir}/man5/xdg-desktop-portal-wlr.5*
