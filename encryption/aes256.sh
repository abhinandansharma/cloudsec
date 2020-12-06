aes256() {
  decodeMe=""
  isPipe="$([ ! -t 0 ] && echo "true" || echo "false")"

  if [ "$1" = '-d' ] || [ "$1" = '--decode' ]; then
    decodeMe="-d"
    shift
  fi

  if [ "$isPipe" = "true" ]; then
    read input
    printf '%s\n' "$input" | openssl aes-256-cbc -a $decodeMe
    exitCode="$?"
  else
    openssl aes-256-cbc -a $decodeMe -in "$*"
    exitCode="$?"
  fi

  unset isPipe decodeMe input
  return "$exitCode"
}
