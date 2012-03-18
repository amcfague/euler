def factor(n):  
  yield 1  
  i = 2  
  limit = n**0.5  
  while i <= limit:  
    if n % i == 0:  
      yield i  
      n = n / i  
      limit = n**0.5  
    else:  
      i += 1  
  if n > 1:  
    yield n  

print list(factor(5000))
