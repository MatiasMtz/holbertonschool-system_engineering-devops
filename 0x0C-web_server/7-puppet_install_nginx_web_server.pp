# Install and configure an Nginx server using Puppet

package { 'nginx':
  ensure => installed
}

file { '/var/www/html/index.html':
  content => 'Hello World',
}

file_line { '/redirect_me 301':
  ensure => present,
  after  => 'listen 80 default_server;',
  path   => '/etc/nginx/sites-available/default',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
