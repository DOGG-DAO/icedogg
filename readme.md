# DOGSHIT (Dogg wrapped shitcoin)

DOGSHIT is a fork of Woofy from YFI.

Inspired by Banteg, It was created during the DOGG DAO Hack-a-thon in order to train non-technical doggs how to launch a smart contract with real value.  It is intended to be forked many times in order to create a fleet of fun furry shitcoins that have some underlying value.

DOGSHIT is a 1/1000 WBNB microcoin forked from Woofy.  An additional 1% tax on every token transfer has been added to DOGSHIT and will be included in all forks belonging to the DAO.  This tax is sent to the multisig of the Council of Guard Dogs.  The Guard Dogs will sell all DOGG coins at frequent intervals for DOGE and BTC.  At the end of each month, all coins will be donated to Dog related charities who accept DOGE.  We already have found one in Chicago.  

It is our hope that if any of our tokens experience real trade volume, a community and proper governance structure will form to focus this giving in other directions, and we look forward to handing over the keys as soon as such a community exists.

You can learn more about our purpose and origins by reading [The DOGG Manifesto](https://app.gitbook.com/@dogg-dao/s/dogg-dao/the-dogg-manifesto-1) and you can join our lively and fun community on [Discord](https://discord.gg/8m5VEDZ5vY)


To fork:

Open contracts/Dogshit.yv:
- set wrap token to the contract address of the token you want to wrap on line 42
- Go to line 52 and change "Dogg Wrapped Shitcoin" to the human name of your coin.  Change the bytes to equal the number of letters and spaces in the name.  
- Go to line 65 and 66.  Change the name and number to match above
- Go to line 71 and 72 and change DOGSHIT to the symbol you want and 

On line 78, now you have to adjust the "Banteg Bonding Curve."  The scaling of tokens basically works by using different decimals on the two contracts.  In the original Woofy, YFI has 18 decimals and woofy has 12.  The difference 6, is the number of 0's involved in scaling so 1,000,000.  1 Woofy is 1/1million wifey.  1/1000 would be a differential of 3.   Most tokens have decimals of 18, but not all of them so check on etherscan and calculate the decimals to get your curve.  Haven't tested, but you should be able to create macrotokens too, by setting the shitcoin to have more decimals than the underlying wrapped token.

Bantag's a special *Woof* bonding curve, allows two-way conversion between the tokens.
That means you can be exposed both to a lighthearted dog coin and the underlying token (WBNB) at the same time.

- Call `dogg` to convert DOGSHIT into BNB.
- Call `undogg` to convert BNB back to DOGSHIT.

####All transfers of DOGSHIT and it's and forks are subject to a 1% tax on each transfer.
You can read more about our governance and taxation on our Manifesto, but this money will traded frequently for DOGE or BTC and donated to charity on a monthly basis.


-- For forks -- update your policy here in the readme...


The DOGG ratio of DOGSHIT is always 1 DOGSHIT = 1,000 WBNB. DOGSHIT is always fully backed by WBNB.

## Deployments

- BSC [`0xfe2e25952e6c8f5c6847e1249a5ff368235f6db5`](https://bscscan.com/token/0xfe2e25952e6c8f5c6847e1249a5ff368235f6db5)

- Trade it on [Apeswap](https://info.apeswap.finance/pair/0x7f24df1a718af253105b6fce1287bf8839588524)
