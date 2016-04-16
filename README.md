# Flask Alembic Ansible Nginx EC2 Template

I love this tool more than any tool I have ever made before.

With this template I can quickly deploy a new webapp to the amazon cloud which logs error messages to slack, has database connectivity, and is configured by Ansible (allowing for idempotent server configuration &mdash; no need to remember server state). 


## Steps To Deploy

### 1. Edit devops/vars.yaml

This file contains the parameters which control ansible. 

**app_name**: unimportant, but is used for naming of some files (probably should just keep it as hello_webapp)
**repo_url**: change this to the url of your github repository
**repo_remote**: which git remote server will use 
**repo_branch**: which git branch server will use 
**src_dir**: the path to where the webapp will be stored on server (probably shouldn't change)
**log_dir**: the path to where logs will be written on the server (probably shouldn't change)
**aws_key_name**: the name of the AWS ssh key which Ansible will use for authentication (must already exist in amazon)
**aws_security_group**: the security group which the spawned server will belong to (security group must already exist)
**aws_instance_name**: the tag which the spawned server will be given &mdash; this is important for identifying your new server in the AWS console
**aws_key_location**: the path on your local computer to the SSH private key associated with aws_key_name listed above &mdash; this file must already exist on your computer
**aws_subnet**: the aws subnet which the spawned server will belong to (this subnet must already exist in your amazon)
**prod_url**: this attribute is not used. I included it because when I add cron jobs via ansible I often make use of this


#### Bash Scripts As Buttons 

I think of bash scripts in my repository as buttons which I am adding to my IDE.
