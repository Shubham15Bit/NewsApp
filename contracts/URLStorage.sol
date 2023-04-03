// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract URLStorage {
    address private owner;
    mapping(uint256 => string) public urls;
    uint256 public urlId;

    constructor() {
        owner = msg.sender;
        urlId = 1;
    }

    modifier onlyOwner() {
        require(
            msg.sender == owner,
            "Only the contract owner can call this function"
        );
        _;
    }

    function setURL(string memory _url) public onlyOwner {
        urls[urlId] = _url;
        urlId = urlId + 1;
    }
}
