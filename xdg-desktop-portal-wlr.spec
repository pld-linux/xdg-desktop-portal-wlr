Summary:	xdg-desktop-portal backend for wlroots
Name:		xdg-desktop-portal-wlr
Version:	0.7.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://github.com/emersion/xdg-desktop-portal-wlr/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	db51a36f9e5bdbbb8623378b3a5588eb
URL:		https://github.com/emersion/xdg-desktop-portal-wlr
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	inih-devel
BuildRequires:	libdrm-devel
BuildRequires:	meson >= 0.58.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pipewire-devel >= 0.3.62
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	scdoc >= 1.9.7
BuildRequires:	systemd-devel
BuildRequires:	wayland-devel
BuildRequires:	wayland-protocols >= 1.24
Requires:	pipewire-libs >= 0.3.62
Requires:	xdg-desktop-portal
Suggests:	grim
Suggests:	slurp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xdg-desktop-portal backend for wlroots.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
