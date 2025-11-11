# Start Fibonacci script
a=0
b=1

echo "Fibonacci sequence up to 10:"

while [ $a -le 10 ]; do
  echo  "$a "
  fn=$((a + b))
  a=$b
  b=$fn
done

echo

