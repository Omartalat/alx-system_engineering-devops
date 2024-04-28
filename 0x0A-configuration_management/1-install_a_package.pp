# Install an especific version of flask (2.1.0)

package { 'Werkzeug':
  pkgname    => 'Werkzeug',
  ensure     => '2.0.0',
  virtualenv => '/path/to/virtualenv',
}

package { 'flask':
  name     => 'flask',
  ensure   => '2.1.0',
  provider => 'pip3',
}
