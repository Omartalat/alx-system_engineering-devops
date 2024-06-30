# using puppet to make changes to our configuration file.

file { '/etc/ssh/ssh_cofig':
  ensure  => present,
  content => "
    # SSH client configuration
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
