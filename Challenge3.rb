def popey(hash_object, *args)
    hash_object.dig(*args)
end

Example1
#users = {"a":{"b":{"c":"d"}}}
#popey(users, :a, :b)


