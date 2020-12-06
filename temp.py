def morse_encode(input_string):
	logMorse = ""
	for x in range(0, len(input_string)):
		c = input_string[x].upper()
		logMorse = logMorse + Config.morseNumericalKeyVal[c]
		print(Config.morseNumericalKeyVal[c])
	return logMorse




class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

ry = Person("Ry", 24)
luke = Person("Luke", 25)



class Person {
	public String name;
	public int age;

	Person(String name, int age) {
		this.name = name;
		this.age = age;
	}
}

Person ry = new Person("Ry", 24);
Person luke = new Person("Luke", 25);