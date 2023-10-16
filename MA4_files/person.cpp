#include <cstdlib>
// Person class 

class Person{
	public:
		Person(int);
		int getAge();
		void setAge(int);
		double getDecades();
		int fib();
		int fibonacci(int);
	private:
		int age;
	};
 
Person::Person(int a){
	age = a;
	}
 
int Person::getAge(){
	return age;
	}
 
void Person::setAge(int a){
	age = a;
	}

double Person::getDecades(){
	return age/10.0;
	}

int Person::fib(){
	return fibonacci(age);
}

int Person::fibonacci(int age){
	 if(age == 0){
		return 0;
		}
	 else if(age == 1){
		return 1;
		}
	 else{
		return fibonacci(age - 1)+fibonacci(age - 2);
		}
}

extern "C"{
	Person* Person_new(int a) {return new Person(a);}
	int Person_getAge(Person* person) {return person->getAge();}
	void Person_setAge(Person* person, int a) {person->setAge(a);}
	double Person_getDecades(Person* person) {return person->getDecades();}
	int Person_fib(Person* person) {return person -> fib();}
	int person_fibonacci(Person* person, int age) {return person -> fibonacci(age);}
	void Person_delete(Person* person){
		if (person){
			delete person;
			person = nullptr;
			}
		}
	}