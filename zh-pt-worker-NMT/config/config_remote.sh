#
# Configuring the remote share (where models & Moses are stored)
# - this may be a local/NFS path or a path on a remote machine
#   (use SSH keys to avoid login prompt!)

#export REMOTE=/root/install/
export LOGIN=ubuntu@54.64.40.131

if [ -n "$LOGIN" ]; then
    LOGIN_RSYNC="-e ssh $LOGIN:" # prepare parameter for rsync
fi

