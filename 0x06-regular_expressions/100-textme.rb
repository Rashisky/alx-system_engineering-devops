#!/usr/bin/env ruby
File.open("text_messages.log", "r") do |file|

    for i in file.readlines()
    line1 =  i.scan(/(?<=from:).*(?=\[flags)/).join("")
    line1 = line1.scan(/\+?\b(?!to|\W)\w+/).join(",")
    line2 = i.scan(/(?<=flags:).*(?=\] \[msg)/).join(",")
    puts i
    puts line1 << "," << line2
    end
end
