#include <iostream>
#include <string>
//#include <array> //not support
#include <sstream> //istringstream
#include <algorithm> //replace

using namespace std;


class Student {
public:
    Student(istringstream &inputInfo);
    ~Student();
    void outputResult();

private:
    string name;
    string studyNum;
    unsigned int age;
    unsigned int grades[4];
    //array<unsigned int,4> grades;
};

Student::Student(istringstream &inputInfo) {
    inputInfo >> this->name >> this->age >> this->studyNum;
    //for(auto &i: this->grades)
    //    inputInfo >> i;
    for(int i=0; i<4; i++) {
        inputInfo >> this->grades[i];
    }
    //inputInfo >> this->grades;
}

Student::~Student() {

}

void Student::outputResult() {
    unsigned int average = 0;
//    for (auto i: this->grades)
//        average+=i;
    for (int i=0; i<4; i++)
        average += this->grades[i];
    average /= 4;
    cout << this->name << "," << this->age << "," <<this->studyNum << "," << average << endl;
}

int main(int argc, char *argv[])
{
    string input;

    //for debug:
    //cout << "Please input your information \n"<<endl;

    cin >> input;
    replace(input.begin(), input.end(),',',' ');

    istringstream inputInfo(input);
    //cout << inputInfo;
    Student stud(inputInfo);
    stud.outputResult();
    return 0;
}

