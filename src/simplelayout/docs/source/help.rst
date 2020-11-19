# Simplelayout Project

> Simplelayout是一个包含命令行接口的简单布局生成器，生成给定分辨率、给定组件大小、给定组件位置的布局方案，以数据格式、图片形式存储，保存到指定目录。

## 命令行接口

**命令行接口：** 采用argparse完成

**接口示例：**
```bash
python simplelayout.py --board_grid 100 --unit_grid 10 --unit_n 3 --positions 1 15 33 --outdir dir1/dir2 --file_name example
```

## 参数

- `--board_grid`:  int，布局板分辨率，代表矩形区域的边长像素数
- `--unit_grid`: int，矩形组件分辨率；**要求** `board_grid` 能整除 `unit_grid`，若不满足退出程序
- `--unit_n`: int，组件数
- `--positions`: 每个元素是 int，数量与 `unit_n` 一致；代表每个组件的位置编号，位置为从1开始的整数，上限为 `(board_grid/unit_grid)^2` ，若不满足要求退出程序
- `-o 或者 --outdir`: str，输出结果的目录，默认为当前目录下的 `example_dir` 目录；若目录不存在程序会自行创建，支持跨平台路径
- `--file_name`: str，输出文件名（不包括文件类型后缀），默认为 `example`

