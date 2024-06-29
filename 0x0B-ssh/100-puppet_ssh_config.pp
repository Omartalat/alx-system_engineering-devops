

file_line{"use the private key ~/.ssh/school":
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => "IdentityFile ~/.ssh/school",
}

file_line{"refuse to authenticate using a password":
 ensure => present,
 path   => '/etc/ssh/ssh_config',
 line   => 'PasswordAuthentication no'
}
 
