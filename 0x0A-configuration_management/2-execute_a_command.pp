exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
  onlyif   => 'pgrep -x killmenow',
}
