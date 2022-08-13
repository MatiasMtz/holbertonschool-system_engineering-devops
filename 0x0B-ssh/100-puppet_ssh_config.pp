# Changing config file with puppet

file_line { 'Declare identity file':
  line    => '    IdentityFile ~/.ssh/school',
  path    => '~/.ssh/config',
  replace => true,
}

file_line { 'Turn off passwd auth':
 ensure => 'present',
 path    => '~/.ssh/config',
 line    => '    PasswordAuthentication no',
 replace => true,
}