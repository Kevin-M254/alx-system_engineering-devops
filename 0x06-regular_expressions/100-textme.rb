#!/usr/bin/env ruby
# Perfoms regex matching on messages
puts ARGV[0].scan(/\[from:(.*)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
