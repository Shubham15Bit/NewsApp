// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract URLStorage {
    address private owner;

    mapping(address => string) private urls;

    constructor() {
        owner = msg.sender;
    }

    modifier OnlyOwner() {
        require(
            msg.sender == owner,
            "Only the contract owner can perform this action"
        );
        _;
    }

    function setURL(address _address, string memory _url) public OnlyOwner {
        urls[_address] = _url;
    }

    function getURL() public view returns (string memory) {
        return urls[msg.sender];
    }

    function getUrlByaddress(
        address _address
    ) public view returns (string memory) {
        return urls[_address];
    }

    function deleteURL(address _address) public OnlyOwner{
        delete urls[_address];
    }
}
