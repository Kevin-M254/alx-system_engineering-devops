# increases the amount of traffic an nginx server can handle

# increase the ULIMIT of the default file
exec { 'fix-for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

#restart nginx

exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
