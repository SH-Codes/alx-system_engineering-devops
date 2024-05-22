# Ensure the Nginx package is installed
package { 'nginx':
  ensure => present,
}

# Update package list and install Nginx
exec { 'install_nginx':
  command  => 'apt-get update && apt-get -y install nginx',
  unless   => 'dpkg -l | grep nginx',
  path     => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
}

# Create an HTML file with "Hello World!"
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  mode    => '0644',
}

# Modify the Nginx default server configuration
exec { 'configure_nginx':
  command  => 'sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/wildreams.tech\/;\\n\\t}/" /etc/nginx/sites-available/default',
  onlyif   => 'grep -q "listen 80 default_server;" /etc/nginx/sites-available/default',
  require  => Package['nginx'],
  path     => ['/usr/bin', '/usr/sbin', '/bin', '/sbin'],
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => Exec['configure_nginx'],
}

