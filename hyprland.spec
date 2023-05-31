Name:           hyprland
Version:        0.25.0
Release:        1%{?dist}
Summary:        Hyprland is a tiling window manager for Linux and other Unix-like systems

License:        MIT
URL:            https://github.com/hyprwm/Hyprland
Source0:        hyprland-0.25.0.tar.gz

BuildRequires: ninja-build
BuildRequires: cmake
BuildRequires: meson
BuildRequires: gcc-c++
BuildRequires: libxcb-devel
BuildRequires: libX11-devel
BuildRequires: pixman-devel
BuildRequires: wayland-protocols-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: wayland-devel
BuildRequires: libdrm-devel
BuildRequires: libxkbcommon-devel
BuildRequires: systemd-devel
BuildRequires: libseat
BuildRequires: xorg-x11-server-Xwayland-devel
BuildRequires: hwdata-devel
BuildRequires: libliftoff-devel
BuildRequires: libdisplay-info-devel

Requires: kitty
Requires: pipewire
Requires: wireplumber
Requires: dunst
Requires: xdg-desktop-portal
Requires: polkit-kde

%description
Hyprland is an innovative window manager that allows multiple desktop workspaces on Linux.


%prep
%autosetup

%build
meson _build
%ninja_build -C _build

%install
%ninja_install -C _build

%files
/usr/local/*
/usr/lib/*
/usr/src/*

%post
sudo cp /usr/local/share/wayland-sessions/hyprland.desktop /usr/share/wayland-sessions

%changelog
* Mon May 29 2023 Robin Mohan <jrobinmohan@gmail.com>
- Made the package
