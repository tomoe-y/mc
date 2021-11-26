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

## TreeImageGenerator.py
- TreeImageGeneratorというクラスが入っている
- ROOTのTTreeのラッパークラスのようなもの
- 各イベントごとに飛跡のグラフを生成して保存するメソッドを持っている
- コンストラクタに目的のtreeが入ったファイルを指定する
    - ワイルドカード使える
### TreeImageGenerator.get_entry
- ほとんどTTree::GetEntry()
### TreeImageGenerator.search_spesific_event
- ある条件を満たすイベントナンバーをメンバ変数 (drawable_event_indexs) にリストとして格納する
### TreeImageGenerator.draw_track
```python3
TreeImageGenerator.draw_track(i: int, is_save_gif=False: bool) -> void:
```
- 引数で指定したイベントの飛跡をmatplotlibの3Dグラフで保存する
- 第二引数 (is_save_gif) がTrueだと3Dグラフを回転させるgifも同時に生成する (めっちゃ時間かかる)
- 保存場所は実行したディレクトリ直下に生成されるimg_tracks内