int find(List integers) {
  int num = integers[0]%2 + integers[1]%2 + integers[2]%2;
  return num < 2 ? integers.where((e) => e.isOdd).toList()[0] : integers.where((e) => e.isEven).toList()[0];
}