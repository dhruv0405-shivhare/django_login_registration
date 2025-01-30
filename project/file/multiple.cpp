/*
in a multiple inheritance we can inherit more than one classes at a time.
jb signature same ho tb diamond problem aati h
*/

#include <iostream>
using namespace std;
class sbi
{
    public:void sbiaccount ()
    {
        cout<<"SBI \n";
    }
};
class axis
{
    public:void axisaccount()
    {
        cout<<"AXIS \n";
    }
};
class customer:public sbi , public axis
{
    public:void msg()
    {
        cout<<"WELCOME \n";
    }
};
int main()
{
    customer ct;
    ct.msg();
    ct.sbiaccount();
    ct.axisaccount();
}
