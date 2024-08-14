# Fixes apache 500 error

exec { 'fix_wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path	  => 'usr/local/bin/:/bin/'
}
