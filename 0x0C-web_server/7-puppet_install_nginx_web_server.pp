#Puppet manifest to install nginx
package { 'nginx':
  ensure   => 'latest',
  name     => 'nginx',
  provider => 'apt'
}

#Check if nginx service is running
service { 'nginx':
  ensure => running,
  enable => true
}

#Check redirection to youtube page
exec { 'redirec':
  provider => 'shell',
  command  => 'sudo sed -i "/server_name _;/ a\\\trewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default'
}

#Check page info
exec { 'index':
  provider => 'shell',
  command  => 'echo "Holberton School" | sudo tee /var/www/html/index.nginx-debian.html'
}
