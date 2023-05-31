## Important note

I have very little experience in making RPM packages. This is one of my first attempts and therefore things

# Hyprland RPM Package for Fedora 38

This project provides an RPM package for the Hyprland window manager for Fedora 38. The package has been compiled from the latest source code and can be installed on recent versions of Fedora Linux.

For making the Spec file, I used the following two tutorials:

https://github.com/hyprwm/Hyprland/discussions/284
@bceric7

https://www.youtube.com/watch?v=ARINIdYXCVE&t=8971s
Titus Tech Talk

## Installation

To install the Hyprland window manager on your Fedora 38 system, you must first download the RPM package from this Github repository. Once the package has been downloaded, you can install it with the following command:

```
sudo dnf install hyprland-0.25.0-1.fc38.x86_64.rpm
```

Once the installation is complete, the Hyprland window manager should be available in your display manager.

## Release Notes

This RPM package has been tested on two devices which both run Fedora 38. Should work on newer versions but there may be some potential compatibility issues.
