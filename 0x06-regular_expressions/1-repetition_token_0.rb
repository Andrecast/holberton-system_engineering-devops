#!/usr/bin/env ruby
# Regular expression to match hbttn, hbtttn, hbttttn, hbtttttn

puts ARGV[0].scan(/hbt{2,5}n/).join
