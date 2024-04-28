# Install an especific version of flask (2.1.0)

package { 'Werkzeug':
  name    => 'Werkzeug',
  ensure     => '2.1.1',
}

package { 'flask':
  name     => 'flask',
  ensure   => '2.1.0',
  provider => 'pip3',
}
