function positive_sum($arr) {
  // Your code here
  $count = count($arr);
  $sum = 0;
  for($i=0;$i<$count;$i++){
    if ($arr[$i] >0){
    $sum += $arr[$i];
    }
    else {
    continue;
    }
  } 
  return $sum;
}