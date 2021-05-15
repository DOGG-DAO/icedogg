# DOGSHIT (Dogg wrapped shitcoin)

DWS is a fork of Woofy from YFI.

It is intended to be forked many times in order to create a fleet of fun furry shitcoins that have some underlying value.

To fork:

Open contracts/Dogshit.yv:
- set wrap token to the contract address of the token you want to wrap on line 31
- Go to line 36 and change "Dogg Wrapped Shitcoin" to the human name of your coin.  Change the bytes to equal the number of letters and spaces in the name.  
- Go to line 46 and 47.  Change the name and number to match above
- Go to line 52 and 53 and change DOGSHIT to the symbol you want and 

Now you have to adjust the "Banteg Bonding Curve."  The scaling of tokens basically works by using different decimals on the two contracts.  In the original Woofy, YFI has 18 decimals and woofy has 12.  The difference 6, is the number of 0's involved in scaling so 1,000,000.  1 Woofy is 1/1million wifey.  1/1000 would be a differential of 3.   Most tokens have decimals of 18, but not all of them so check on etherscan and calculate the decimals to get your curve.  Haven't tested, but you should be able to create macrotokens too, by setting the shitcoin to have more decimals than the underlying wrapped token.

Bantag's a special *Woof* bonding curve, allows two-way conversion between the tokens.
That means you can be exposed both to a lighthearted dog coin and the DeFi darling blue chip at the same time.

- Call `dogg` to convert DOGSHIT into BNB.
- Call `undogg` to convert BNB back to DOGSHIT.

####All transfers of DOGSHIT and it's and forks are subject to a 0.1% tax on each transfer.
You can read more about our governance and taxation on our Manifesto, but this money will traded frequently for DOGE or BTC and donated to charity on a monthly basis.


-- For forks -- update your policy here in the readme...


The DOGG ratio of DOGSHIT is always 1 DOGSHIT = 1,000 WBNB. DOGSHIT is always fully backed by YFI.

## Deployments

- Ethereum Mainnet [`0xfe2e25952e6c8f5c6847e1249a5ff368235f6db5`](https://bscscan.com/token/0xfe2e25952e6c8f5c6847e1249a5ff368235f6db5)
