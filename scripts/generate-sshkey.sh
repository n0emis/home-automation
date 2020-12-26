FILE=/tmp/${1}

ssh-keygen -t ed25519 -f $FILE -N "" -C "$1"

PRIV=$(base64 -w 0 < $FILE)
PUB=$(base64 -w 0 < $FILE.pub)


echo "${PRIV}

pub: ${PUB}" | pass insert -m infra/$1/ssh

rm $FILE
rm ${FILE}.pub
