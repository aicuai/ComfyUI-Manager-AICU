# ComfyUI Manager 日本語訳

**ComfyUI-Manager** は [ComfyUI](https://github.com/comfyanonymous/ComfyUI)の使い勝手を高めるための拡張機能です。ComfyUIにおけるカスタムノードの **インストール / 削除 / 無効化 / 有効化** を行う機能を提供します。さらにComfyUI内の情報へのアクセスを便利にするハブ機能や便利機能も提供します。

![menu](https://raw.githubusercontent.com/ltdrdata/ComfyUI-extension-tutorials/refs/heads/Main/ComfyUI-Manager/images/dialog.jpg)

## NOTICE
* V3.16: `uv` のサポートが追加されました。`config.ini` で `use_uv` を設定してください。
* V3.10: `ダブルクリック機能` は削除されました。
  * この機能は https://github.com/ltdrdata/comfyui-connection-helper に移動しました。
* V3.3.2: 大幅に刷新されました。公式に [https://registry.comfy.org/](https://registry.comfy.org/) をサポートします。
* 全てのノード情報は [ComfyUI Nodes Info](https://ltdrdata.io/) ページで確���できます。

## インストール

### インストール[方法1] (一般的なインストール方法: ComfyUI-Manager のみ)

既存の ComfyUI に加えて ComfyUI-Manager をインストールするには、以下の手順に従ってください。

1. ターミナル（またはコマンドプロンプト）で `ComfyUI/custom_nodes` ディレクトリに移動します。
2. `git clone https://github.com/ltdrdata/ComfyUI-Manager comfyui-manager` を実行します。
3. ComfyUI を再起動します。


### インストール[方法2] (ポータブル版 ComfyUI へのインストール: ComfyUI-Manager のみ)
1. git をインストールします。
- https://git-scm.com/download/win
- スタンドアロン版
- オプション: `use windows default console window` を選択
2. [scripts/install-manager-for-portable-version.bat](https://github.com/ltdrdata/ComfyUI-Manager/raw/main/scripts/install-manager-for-portable-version.bat) をインストール済みの `"ComfyUI_windows_portable"` ディレクトリにダウンロードします。
- クリックしないでください。リンクを右クリックして「名前を付���て保存...」を使用してください。
3. `install-manager-for-portable-version.bat` バッチファイルをダブルクリックします。

![portable-install](https://raw.githubusercontent.com/ltdrdata/ComfyUI-extension-tutorials/Main/ComfyUI-Manager/images/portable-install.jpg)


### インストール[方法3] (comfy-cli を介したインストール: ComfyUI と ComfyUI-Manager を一度にインストール)
> 推奨: comfy-cli は、CLI から ComfyUI を管理するための様々な機能を提供します。

* **前提条件: python 3, git**

Windows:
```commandline
python -m venv venv
venv\Scripts\activate
pip install comfy-cli
comfy install
```

Linux/OSX:
```commandline
python -m venv venv
. venv/bin/activate
pip install comfy-cli
comfy install
```
* 参照: https://github.com/Comfy-Org/comfy-cli


### インストール[方法4] (linux+venv へのインストール: ComfyUI + ComfyUI-Manager)

venv 環境を使用して Linux に ComfyUI と ComfyUI-Manager をインストールするには、以下の手順に従ってください。
* **前提条件: python-is-python3, python3-venv, git**

1. [scripts/install-comfyui-venv-linux.sh](https://github.com/ltdrdata/ComfyUI-Manager/raw/main/scripts/install-comfyui-venv-linux.sh) を空のインストールディレクトリにダウンロードします。
- クリックしないでください。リンクを右クリックして「名前を付けて保存...」を使用してください。
- ComfyUI は指定されたディレクトリのサブディレクトリにインストールされ、そのディレクトリには生成された実行可能スクリプトが含まれます。
2. `chmod +x install-comfyui-venv-linux.sh` を実行します。
3. `./install-comfyui-venv-linux.sh` を実行します。

### インストール時の注意点
* **DO**: `ComfyUI-Manager` のファイルは、`ComfyUI/custom_nodes/comfyui-manager` のパスに正確に配置されている必要があります。
  * 圧縮ファイル形式でのインストールは推奨されません。
* **DON'T**: `ComfyUI/custom_nodes` の場所に直接解凍しないでください。`__init__.py` など、Managerのファイルがそのディレクトリに直接配置されてしまいます。
  * `ComfyUI/custom_nodes` から���べての ComfyUI-Manager ファイルを削除する必要があります。
* **DON'T**: `ComfyUI/custom_nodes/ComfyUI-Manager/ComfyUI-Manager` のようなパスに解凍しないでください。
* **DON'T**: `ComfyUI/custom_nodes/ComfyUI-Manager-main` のようなパスに解凍しないでください。
  * このような場合、`ComfyUI-Manager` は動作するかもしれませんが、`ComfyUI-Manager` 内で認識されず、更新を実行できません。また、重複インストールのリスクもあります。削除して `git clone` メソッドで適切にインストールしてください。


システム構成に応じて、`./run_gpu.sh` または `./run_cpu.sh` を実行して ComfyUI を起動できます。

## Colab Notebook
このリポジトリは、ComfyUI-Manager を含む ComfyUI をインストールして使用できる Colab ノートブックを提供します。ComfyUI を使用するには、[このリンクをクリックしてください](https://colab.research.google.com/github/ltdrdata/ComfyUI-Manager/blob/main/notebooks/comfyui_colab_with_manager.ipynb)。
* ComfyUI のインストールをサポート
* ComfyUI-Manager の基本的なインストールをサポート
* Colab ノートブックの再起動時にカスタムノードの依存関係を自動的にインストールする機能をサポート


## 使用方法

1. メインメニューの「Manager」ボタンをクリックします。

    ![mainmenu](https://raw.githubusercontent.com/ltdrdata/ComfyUI-extension-tutorials/Main/ComfyUI-Manager/images/topbar.jpg)


2. 「Install Custom Nodes」または「Install Models」をクリックすると、インストーラーダイアログが開きます。

    ![menu](https://raw.githubusercontent.com/ltdrdata/ComfyUI-extension-tutorials/refs/heads/Main/ComfyUI-Manager/images/dialog.jpg)

    * 3つのDBモードがあります: `DB: Channel (1day cache)`, `DB: Local`, `DB: Channel (remote)`。
      * `Channel (1day cache)` は、1日有効なキャッシュ情報を使用し、リストを素早く表示します。
        * この情報は、キャッシュがない場合、キャッシュの有効期限が切れた場合、またはチャンネル（リモート）を介して外部情報が取得された場合に更新されます��
        * ComfyUI を新たに起動するたびに、このモードが常に**デフォルト**モードとして設定されます。
      * `Local` は、ComfyUI-Manager にローカルに保存されている情報を使用します。
        * この情報は、ComfyUI-Manager を更新した場合にのみ更新されます。
        * カスタムノード開発者は、`custom-node-list.json` にノードを登録してテストする際にこのモードを使用する必要があります。
      * `Channel (remote)` は、リモートチャンネルから情報を取得し、常に最新のリストを表示します。
      * ネットワークエラーにより取得できない場合は、強制的にローカル情報を使用します。

    * `Fetch Updates` メニューは、カスタムノードの更新データをローカルで取得します。実際の更新は、「Install Custom Nodes」メニューの「Update」ボタンをクリックすることで適用されます。

3. 「Install」または「Try Install」ボタンをクリックします。

    ![node-install-dialog](https://raw.githubusercontent.com/ltdrdata/ComfyUI-extension-tutorials/Main/ComfyUI-Manager/images/custom-nodes.jpg)

    ![model-install-dialog](https://raw.githubusercontent.com/ltdrdata/ComfyUI-extension-tutorials/Main/ComfyUI-Manager/images/models.jpg)

    * Installed: この項目はすでにインストールされています。
    * Install: このボタンをクリックすると、項目がインストールされます。
    * Try Install: インストール情報が確認できないカスタムノードです。ボタンをクリックしてインストールを試行します。

    * 上部に赤い背景の `Channel` インジケーターが表示されている場合、それはデフォルトチャンネルではないことを意味します。保持されている情報量がデフォルトチャンネルとは異なるため、このチャンネル状態では多くのカスタムノードが表示されない場合があります。
      * チャンネル設定は、ノードリストだけでなく、「Update all」のようなすべての機能に広範な影響を与えます。
    * 黄色い背景の Conflicted Nodes は、それぞれの拡張機能で他の拡張��能と競合しているノードのリストを表示します。この問題は開発者によって対処される必要があり、ユーザーはこれらの競合により一部のノードが正しく機能しない可能性があり、それに応じてインストールする必要があることに注意してください。

4. 共有
  ![menu](https://raw.githubusercontent.com/ltdrdata/ComfyUI-extension-tutorials/Main/ComfyUI-Manager/images/topbar.jpg) ![share](https://raw.githubusercontent.com/ltdrdata/ComfyUI-extension-tutorials/Main/ComfyUI-Manager/images/share.jpg)

  * メインメニュー下部の共有ボタンをクリックするか、Imageノードのコンテキストメニューにある「Share Output」を選択することで、ワークフローを共有できます。
  * 現在、[https://comfyworkflows.com/](https://comfyworkflows.com/)、[https://openart.ai](https://openart.ai/workflows/dev)、[https://youml.com](https://youml.com) を介した共有、および Matrix チャンネルを介した共有をサポートしています。

  ![menu](https://raw.githubusercontent.com/ltdrdata/ComfyUI-extension-tutorials/Main/ComfyUI-Manager/images/share-setting.jpg)

  * Manager メニューの共有設定から、メインメニューの共有ボタンまたはコンテキストメニューの共有出力ボタンの動作を設定できます。
    * `None`: メインメニューから非表示
    * `All`: ユーザーが共有するタイトルを選択できるダイアログを表示

## パス
`ComfyUI-Manager` V3.0 以降では、設定ファイルと動的に生成されるファイルは `<USER_DIRECTORY>/default/ComfyUI-Manager/` の下に配置されます。

* <USER_DIRECTORY>
  * オプションなしで実行された場合、パスはデフォルトで `ComfyUI/user` になります。
  * `--user-directory <USER_DIRECTORY>` を使用して設定できます。

* 基本設定ファイル: `<USER_DIRECTORY>/default/ComfyUI-Manager/config.ini`
* 設定可能なチャンネルリスト: `<USER_DIRECTORY>/default/ComfyUI-Manager/channels.ini`
* 設定可能な pip オーバーライド: `<USER_DIRECTORY>/default/ComfyUI-Manager/pip_overrides.json`
* 設定可能な pip ブラックリスト: `<USER_DIRECTORY>/default/ComfyUI-Manager/pip_blacklist.list`
* 設定可能な pip 自動修正: `<USER_DIRECTORY>/default/ComfyUI-Manager/pip_auto_fix.list`
* 保存されたスナップショットファイル: `<USER_DIRECTORY>/default/ComfyUI-Manager/snapshots`
* 起動スクリプトファイル: `<USER_DIRECTORY>/default/ComfyUI-Manager/startup-scripts`
* コンポーネントファイル: `<USER_DIRECTORY>/default/ComfyUI-Manager/components`


## `extra_model_paths.yaml` 設定
以下の設定は、`is_default` とマークされたセクションに基づいて適用されます。

* `custom_nodes`: カスタムノードをインストールするためのパス
    * インポートは `is_default` として設定されたパスに従う必要はありませんが、これは `ComfyUI Nodes Manager` によってカスタムノードがインストールされるパスです。
* `download_model_base`: モデルをダウンロードするためのパス


## スナップショットマネージャー
* 「Save snapshot」を押すか、「Manager Menu」で「Update All」を使用すると、現在のイ���ストール状態のスナップショットが保存されます。
  * スナップショットファイルディレクトリ: `<USER_DIRECTORY>/default/ComfyUI-Manager/snapshots`
  * スナップショットファイルの名前を変更できます。
* 「Restore」ボタンを押すと、それぞれのスナップショットのインストール状態に戻すことができます。
  * ただし、Git で管理されていないカスタムノードの場合、スナップショットのサポートは不完全です。
* 「Restore」を押すと、次回の ComfyUI 起動時に有効になります。
  * 選択されたスナップショットファイルは `<USER_DIRECTORY>/default/ComfyUI-Manager/startup-scripts/restore-snapshot.json` に保存され、ComfyUI の再起動時にスナップショットが適用されてから削除されます。

![model-install-dialog](https://raw.githubusercontent.com/ltdrdata/ComfyUI-extension-tutorials/Main/ComfyUI-Manager/images/snapshot.jpg)


## cm-cli: パワーユーザー向けコマンドラインツール
* ComfyUI を実行せずに ComfyUI-Manager の機能を使用で���るツールが提供されています。
* 詳細については、[cm-cli ドキュメント](docs/en/cm-cli.md) を参照してください。


## ComfyUI-Manager にカスタムノードを登録する方法

* ComfyUI-Manager のルートにある `custom-node-list.json` にエントリを追加し、プルリクエストを送信してください。
* 注: 変更を加えて PR を送信する前に、「Use local DB」をチェックし、「Install custom nodes」ダイアログで拡張機能リストが問題なくロードされることを確認してください。時折、カンマの不足や余分なカンマが JSON 構文エラーにつながることがあります。
* 残りの JSON は将来的にスクリプトを通じて更新されるため、心配する必要はありません。


## カスタムノードサポートガイド

* **注意:**
    - GitHub リポジトリ名が `custom_nodes` 下のサブディレクトリ名と一致すると仮定すべきではありません。`custom_nodes` 下のサブディレクトリ名は、`pyproject.toml` の `name` フィールドの正規化された名前を使用するようになります。
    - 可能な限り、インポートにディレクトリ名に依存しないようにしてください。

* https://docs.comfy.org/registry/overview
* https://github.com/Comfy-Org/rfcs

**特殊目的ファイル** (オプション)
  * `pyproject.toml` - comfyregistry の仕様ファイル。
  * `node_list.json` - `NODE_CLASS_MAPPINGS` のカスタムノードパターンが慣習的でない場合、参照用にノードのリストを手動で提供するために使用されます。([例](https://github.com/melMass/comfy_mtb/raw/main/node_list.json))
  * `requirements.txt` - インストール時に、この pip requirements が自動的にインストールされます。
  * `install.py` - インストール時に自動的に呼び出されます。
  * **すべてのスクリプトは、対応するカスタムノードのルートパスから実行されます。**


## コンポーネント共有
* **コピー＆ペースト**
  * [デモページ](https://ltdrdata.github.io/component-demo/)
  * クリップボードからコンポーネントを貼り付ける場合、以下の JSON 形式のテキストをサポートします。(text/plain)
    ```
    {
      "kind": "ComfyUI Components",
      "timestamp": <現在のタイムスタンプ>,
      "components":
        {
          <コンポーネント名>: <コンポーネントノードデータ>
        }
    }
    ```
  * `<現在のタイムスタンプ>` タイムスタンプは常に一意であることを確認してください。
    * "components" は、`<USER_DIRECTORY>/default/ComfyUI-Manager/components` に保存されているファイルのコンテンツと同じ構造である必要があります。
      * `<コンポーネント名>`: 名前は `<prefix>::<node name>` の形式である必要があります。
        * `<コンポーネントノードデータ>`: グループノードのノードデータ内。
          * `<version>`: `major.minor.patch` また��� `major.minor` の2つの形式のみが許可されます。(例: `1.0`, `2.2.1`)
          * `<datetime>`: 保存時間
          * `<packname>`: packname が空でない場合、カテゴリは `packname/workflow` となり、`<USER_DIRECTORY>/default/ComfyUI-Manager/components` の `<packname>.pack` ファイルに保存されます。
          * `<category>`: カテゴリも packname もない場合、components カテゴリに保存されます。
          ```
              "version":"1.0",
              "datetime": 1705390656516,
              "packname": "mypack",
              "category": "util/pipe",
          ```
* **ドラッグ＆ドロップ**
  * `.pack` または `.json` ファイルをドラッグ＆ドロップすると、対応するコンポーネントが追加されます。
  * 例のパック: [Impact.pack](misc/Impact.pack)

* 単一のコンポーネントをドラッグ＆ドロップまたは貼り付けるとノードが追加されます。ただし、複数のコンポーネントを追加してもノードは追加されません。


## 不足ノードのインストールサポート

![missing-menu](https://raw.githubusercontent.com/ltdrdata/ComfyUI-extension-tutorials/Main/ComfyUI-Manager/images/missing-menu.jpg)

* メニューの「Install Missing Custom Nodes」ボタンをクリックすると、現在ワークフローに存在しないノードを含む拡張ノードのリストが表示されます。

![missing-list](https://raw.githubusercontent.com/ltdrdata/ComfyUI-extension-tutorials/Main/ComfyUI-Manager/images/missing-list.jpg)


# 設定
* `config.ini` ファイルを修正して、ComfyUI-Manager の設定を適用できます。
    * ComfyUI-Manager が使用する `config.ini` へのパスは、起動ログメッセージに表示されます。
    * 参照: [https://github.com/ltdrdata/ComfyUI-Manager#paths]
* 設定オプション:
    ```
    [default]
    git_exe = <git 実行可能ファイルへのパスを手動で指定します。空の場合、デフォルトの git 実行可能パスが使用されます。>
    use_uv = <依存関係のインストールに pip の代わりに uv を使用します。>
    default_cache_as_channel_url = <���動時に channel_url として指定された DB を取得するかどうかを決定します。>
    bypass_ssl = <SSL エラーが発生した場合に SSL を無効にするには True に設定します。>
    file_logging = <ComfyUI-Manager が使用するログファイルを作成するかどうかを設定します。>
    windows_selector_event_loop_policy = <Windows でイベントループエラーが発生した場合、これを True に設定します。>
    model_download_by_agent = <モデルをダウンロードする際に、torchvision_download_url の代わりにエージェントを使用します。>
    downgrade_blacklist = <ダウングレードを防ぐパッケージのリストを設定します。カンマで区切ってリストします。>
    security_level = <セキュリティレベルを設定します => strong|normal|normal-|weak>
    always_lazy_install = <Windows 以外の環境でも再起動時に依存関係のインストールを実行するかどうか。>
    network_mode = <ネットワークモードを設定します => public|private|offline>
    ```

    * network_mode:
      - public: 一般的なパブリックネットワークを使用する環境。
      - private: `channel_url` でプライベートノードDBが設定されているクローズドネットワークを使用する環境。(キャッシュが利用可能な場合はキャッシュを使用)
      - offline: オフラインネットワークを使用する際に、外部接続を一切使用しない環境。(キャッシュが利用可能な場合はキャッシュを使用)


## 追加機能
* ファイルへのログ出力機能
  * この機能はデフォルトで有効になっており、`config.ini` で `file_logging = False` に設定することで無効にできます。

* ノードの修正（再作成）: ノードを右クリックして「Fix node (recreate)」を選択すると、ノードを再作成できます。ウィジェットの値はリセットされますが、接続は同じ名前のものを維持します。
  * これは、以前作成された古いワークフローのノードで、カスタムノードのバージョン変更と互換性がない場合にエラーを修正するために使用されます。

* ノードタイトルのダブルクリック: ComfyUI-Manager メニューでノードのダブルクリック動作を設定できます。
  * `Copy All Connections`, `Copy Input Connections`: ノードをダブルクリックすると、最も近いノードの接続がコピーされます。
    * このアクションは、ノードの中心から1000ピクセル以内の直線距離にある最も近いノードを対象とします。
    * `Copy All Connections` の場合、既存の出力を複製しますが、重複する接続は許可されないため、元のノードの既存の出力接続は切断されます。
    * この機能は、名前が一致する入力と出力のみをコピーします。

  * `Possible Input Connections`: 指定された範囲内で最も近いタイプに一致するすべての出力を接続します。
    * この接続は、ターゲットノードの左側に配置されたノードの中で最も近い出力にリンクします。

  * `Possible(left) + Copy(right)`: タイトルの左半分をダブルクリックすると `Possible Input Connections` として動作し、右半分をダブルクリックすると `Copy All Connections` として動作します。

* 特定のパッケージのダウングレード防止
  * `config.ini` ファイルの `downgrade_blacklist` セクションにパッケージ名をカンマで区切ってリストします。
    * 例:
    ```
      downgrade_blacklist = diffusers, kornia
    ```

* カスタム pip マッピング
  * `pip_overrides.json` ファイルを作成すると、特定の pip パッケージのインストールがユーザー定義のインストールに変更されます。
    * `pip_overrides.json.template` ファイルを参照してください。

* 特定の pip パッケージのインストール防止
  * `pip_blacklist.list` ファイルにパッケージ名を1行に1つずつリストします。

* pip インストールの自動復元
 * `pip_auto_fix.list` に `requirements.txt` と同様に pip の要件をリストすると、ComfyUI の起動時や、様々なカスタムノードのインストール中にバージョンが不一致になった場合に、指定されたバージョンに自動的に��元されます。
 * `--index-url` を使用できます。

* `aria2` をダウンローダーとして使用
  * [方法](docs/en/use_aria2.md)


## 環境変数

以下の機能は環境変数を使用して設定できます。

* **COMFYUI_PATH**: ComfyUI のインストールパス
* **GITHUB_ENDPOINT**: GitHub へのアクセスが制限されている環境でのリバースプロキシ設定
* **HF_ENDPOINT**: Hugging Face へのアクセスが制限されている環境でのリバースプロキシ設定


### 例1:
`https://github.com/ltdrdata/ComfyUI-Impact-Pack` を `https://mirror.ghproxy.com/https://github.com/ltdrdata/ComfyUI-Impact-Pack` にリダイレクトする

```
GITHUB_ENDPOINT=https://mirror.ghproxy.com/https://github.com
```

#### 例2:
`https://huggingface.co/path/to/somewhere` を `https://some-hf-mirror.com/path/to/somewhere` に変更する

```
HF_ENDPOINT=https://some-hf-mirror.com
```

## スキャナー
`scan.sh` スクリプトを実行すると:

* `extension-node-map.json` が更新されます。
  * これを行うには、`custom-node-list.json` にリストされているカスタムノー���を `~/.tmp/default` にプルまたはクローンします。
  * このステップをスキップするには、`--skip-update` オプションを追加します。
  * `~/.tmp/default` 以外のパスを指定したい場合は、`scan.sh` の代わりに `python scanner.py [path]` を直接実行します。

* `github-stats.json` が更新されます。
  * これは GitHub API を使用するため、レート制限にすぐに達して機能しなくなるのを避けるために、`export GITHUB_TOKEN=your_token_here` でトークンを設定してください。
  * このステップをスキップするには、`--skip-update-stat` オプションを追加します。

* `--skip-all` オプションは、`--skip-update` と `--skip-stat-update` の両方を適用します。


## トラブルシューティング
* `git.exe` がシステム git 以外の特定の場所にインストールされている場合、ComfyUI-Manager をインストールして ComfyUI を実行してください。その後、生成される `<USER_DIRECTORY>/default/ComfyUI-Manager/config.ini` ファイルの `git_exe =` の箇所にファイル名を含めたパスを指定してください。
* ComfyUI-Manager 自体の更新に失敗した場合、**ComfyUI-Manager** ディレクトリに移動し、`git update-ref refs/remotes/origin/main a361cc1 && git fetch --all && git pull` コマンドを実行してください。
* Windows で `Overlapped Object has pending operation at deallocation on Comfyui Manager load` エラーが発生した場合
  * `config.ini` ファイルを編集: `windows_selector_event_loop_policy = True` を追加します。
* `SSL: CERTIFICATE_VERIFY_FAILED` エラーが発生した場合。
  * `config.ini` ファイルを編集: `bypass_ssl = True` を追加します。


## セキュリティポリシー
  * `config.ini` ファイルを編集: `security_level = <LEVEL>` を追加します。
    * `strong`
      * `high` および `middle` レベルのリスクのある機能は許可されません。
    * `normal`
      * `high` レベルのリスクのある機能は許可されません。
      * `middle` レベルのリスクのある機能は利用可能です。
    * `normal-`
      * `--listen` が指定されており、`127.` で始まらな��場合、`high` レベルのリスクのある機能は許可されません。
      * `middle` レベルのリスクのある機能は利用可能です。
    * `weak`
      * すべての機能が利用可能です。

  * `high` レベルのリスクのある機能
    * `Install via git url`, `pip install`
    * `default channel` に登録されていないカスタムノードのインストール。
    * カスタムノードの修正

  * `middle` レベルのリスクのある機能
    * アンインストール/更新
    * `default channel` に登録されているカスタムノードのインストール。
    * スナップショットの復元/削除
    * 再起動

  * `low` レベルのリスクのある機能
    * ComfyUI の更新


# 免責事項

* この拡張機能は、カスタムノードのインストールを便利にする機能を提供するものであり、それらが適切に機能することを保証するものではありません。


## クレジット
ComfyUI/[ComfyUI](https://github.com/comfyanonymous/ComfyUI) - 強力でモジュール式の安定拡散 GUI。

**そして、すべての ComfyUI カスタムノード開発者の皆様へ**