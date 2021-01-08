# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
# Absolute path this script is in, thus /home/user/bin
SCRIPTPATH=$(dirname "$SCRIPT")
mkdir -p "$SCRIPTPATH/out/"
envsubst < "$SCRIPTPATH/"template.conf > "$SCRIPTPATH/out/$TEST_VAR".conf