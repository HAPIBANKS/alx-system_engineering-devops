# Using strace, find out why Apache is returning a 500 error
# fix it and then automate it using Puppet
exec {'sed phpp':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
  onlyif  => 'test -f /var/www/html/wp-settings.php',
}
