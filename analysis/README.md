# Usage
## showParticleName.C
- rootマクロ
- ROOT Treeに各粒子がいくつ入ってたかを出力する
- TDatabasePDGには pdgcode > 1000000000 の粒子情報は入っていなかったのでカウントから除外した
```bash
[user@host mc]$ root
root [0] .x showParticleName.C("/path/to/rootfile")
```
もしくは
```bash
[user@host mc]$ root 'showParticleName.C("/path/to/rootfile")'
```
- TChainでファイルの読み込みを行っているので引数にワイルドカードを使える
```bash
[user@host mc]$ root 'showParticleName.C("/path/to/test_*.root")'
```