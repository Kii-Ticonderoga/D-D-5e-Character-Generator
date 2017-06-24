stats = {"STR"=>[nil,nil],"DEX"=>[nil,nil],"CON"=>[nil,nil],"INT"=>[nil,nil],"WIS"=>[nil,nil],"CHA"=>[nil,nil]}
stats.keys.each { |i| stats[i][0]=rand(6..18)
stats[i][1] = (stats[i][0]-10)/2.to_i }
stats.each { |k,v| puts "#{k} = " + v[0].to_s + ", " + (v[1].to_i>0?"+":"") + v[1].to_s }
