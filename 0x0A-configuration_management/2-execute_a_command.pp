# killing process

exec { "pkill -f killmenow":
  path => "/usr/bin:/bin/:/usr/local/bin"
}