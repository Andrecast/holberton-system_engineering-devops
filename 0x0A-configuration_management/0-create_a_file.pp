# Creating a file in /tmp directory
file {'/tmp/holberton':
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet'
}
