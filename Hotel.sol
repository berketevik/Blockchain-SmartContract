pragma solidity >=0.4.22 <0.9.0;

contract Hotel{
    
    //-----------------------------------------------------------------------
    string public functionCalled;
    bool public Check_In;
    
    //THIS IS HOTEL OWNERS ADRESS
    address payable public  owner = msg.sender ;
    
    //We are using theese 2 methods to transfer ethereum from customer to contract
    function sendEther() external payable {
        functionCalled = 'sendEther';
    }
    
    function() external payable {
        functionCalled = 'fallback';
    }
    
    //we are using this method to transfer ethereum on contract to hotel owners account
    function check_in() public {
        //if check-in button clicked , ethereum goes from contract to hotel owner.
        //adresss   transfer   amount   FROM CONTRACT 
        owner.transfer(address(this).balance);
        Check_In=true;
    }
    
    //this method takes money from contract to customer back
    function cancel() public {
        //this return contracts balance to customer
        //adresss   transfer   amount  TO CONTRACT 
        msg.sender.transfer(address(this).balance);
    }
    
    //this method return contracts balance as wei without using any gas.
     function balanceOfSC() public view returns(uint256){
        return address(this).balance;
    }
}