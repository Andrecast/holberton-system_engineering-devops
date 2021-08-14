# Excecute a command
exec {'kill_process':
  command  => 'pkill killmenow',
  provider => 'shell'
}
