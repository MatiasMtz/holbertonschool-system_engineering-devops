#!/usr/bin/env ruby
#Ruby script with regular expression matching method
puts ARGV[0].scan(/^\d{10}$/).join
