# AWS CloudFormation Script

## Overview
To provision and configure your stack resources, you must understand AWS
CloudFormation templates, which are formatted text files in JSON or YAML. 
These templates describe the resources that you want to provision in your
AWS CloudFormation stacks. You can use the AWS CloudFormation Designer or
any text editor to create and save templates.

## Description
* **aws_cft.json** - template is used to create an Amazon EC2 instance in an
Amazon EC2 security group.
* **aws_gpu_cft.json** - template is used to create an Amazon EC2 instance in an
Amazon EC2 security group with NVIDIA GPU drivers and toolkit installed.
* **aws_tensorflow_gpu_cft.json** - template is used to create an Amazon EC2 instance
in an Amazon EC2 security group with Tensorflow 0.11 and NVIDIA GPU drivers and toolkit
installed.
* **aws_gpu_docker_cft.json** - template is used to create an Amazon EC2 instance in an Amazon EC2 security group with the latest NVIDIA graphics drivers and Docker.

## Prerequisites
Must provide the right credentials. You can create a key pair using the
Amazon EC2 console or the command line. After you create a key pair, you
can specify it when you launch your instance.

## Parameters
Inside the **aws_cft_deploy.sh** file, you need to specify the following parameters:
* stack-name
* template-body
* ParameterKey
* KeyName
* SSHLocation
* Volume

## Example Usage
1. Modify the parameter values accordingly in the **aws_cft_deploy.sh** script.
2. Run the shell script:
```
bash aws_cft_deploy.sh
```

## Additional Notes
### AWS GPU Docker CloudFormation Template
#### What is Nouveau, and why do you need to disable it?
Ubuntu has enabled Kernel Nouveau Driver, which is a display driver for NVIDIA GPUs, 
developed as an open-source project through reverse engineering of the NVIDIA driver.
It ships by default with many Linux distributions as the default display driver for 
NVIDIA hardware. It is not developed or supported by NVIDIA, and it is not related to 
the NVIDIA driver, other than the fact that both Nouveau and the NVIDIA driver are
capable of driving NVIDIA GPUs. Only one driver can control a GPU at a time, so if a 
GPU is being driven by the Nouveau driver, Nouveau must be disabled before installing
the NVIDIA driver.

Nouveau performs modesets in the kernel. This can make disabling Nouveau difficult, 
as the kernel modeset is used to display a framebuffer console, which means that 
Nouveau will be in use even if X is not running. As long as Nouveau is in use, its 
kernel module cannot be unloaded, which will prevent the NVIDIA kernel module from 
loading. It is therefore important to make sure that Nouveau's kernel modesetting 
is disabled before installing the NVIDIA driver.

#### How do I prevent Nouveau from loading and performing a kernel modeset?
A simple way to prevent Nouveau from loading and performing a kernel modeset is to 
add configuration directives for the module loader to a file in /etc/modprobe.d/. 
These configuration directives can technically be added to any file in /etc/modprobe.d/, 
but many of the existing files in that directory are provided and maintained by your 
distributor, which may from time to time provide updated configuration files which 
could conflict with your changes. Therefore, it is recommended to create a new file, 
for example, /etc/modprobe.d/disable-nouveau.conf, rather than editing one of the 
existing files, such as the popular /etc/modprobe.d/blacklist.conf. Note that some
module loaders will only look for configuration directives in files whose names 
end with .conf, so if you are creating a new file, make sure its name ends with .conf.

Whether you choose to create a new file or edit an existing one, the following 
two lines will need to be added:

* blacklist nouveau
* options nouveau modeset=0

The first line will prevent Nouveau's kernel module from loading automatically 
at boot. It will not prevent manual loading of the module, and it will not prevent 
the X server from loading the kernel module; see "How do I prevent the X server 
from loading Nouveau?" below. The second line will prevent Nouveau from doing 
a kernel modeset. Without the kernel modeset, it is possible to unload Nouveau's 
kernel module, in the event that it is accidentally or intentionally loaded.

If nvidia-installer detects Nouveau is in use by the system, it will offer to 
create such a modprobe configuration file to disable Nouveau.

Source: 
Refer to 8.1. Interaction with the Nouveau Driver
http://us.download.nvidia.com/XFree86/Linux-x86/367.44/README/commonproblems.html 
