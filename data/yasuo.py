import os
import ffmpeg
import shutil
from multiprocessing import Pool, cpu_count

def process_single_file(args):
    """
    处理单个文件的函数（用于多进程）
    """
    file_info, src_root, dst_root = args
    root, file = file_info
    
    src_path = os.path.join(root, file)
    
    # 相对路径，保持目录结构
    rel_path = os.path.relpath(root, src_root)
    dst_dir = os.path.join(dst_root, rel_path)
    os.makedirs(dst_dir, exist_ok=True)
    
    file_ext = os.path.splitext(file)[1].lower()
    
    if file_ext == ".wav":
        # WAV 文件转换为 MP3
        dst_filename = os.path.splitext(file)[0] + ".mp3"
        dst_path = os.path.join(dst_dir, dst_filename)
        
        # 若已存在则跳过
        if os.path.exists(dst_path):
            return f"跳过已存在: {dst_path}"
        
        try:
            (
                ffmpeg
                .input(src_path)
                .output(dst_path, format="mp3", audio_bitrate="192k")
                .overwrite_output()
                .run(quiet=True)
            )
            return f"转换成功: {src_path} -> {dst_path}"
        except ffmpeg.Error as e:
            return f"转换失败: {src_path}, 错误: {e.stderr.decode()}"
            
    elif file_ext == ".mp3":
        # MP3 文件直接复制
        dst_path = os.path.join(dst_dir, file)
        
        # 若已存在则跳过
        if os.path.exists(dst_path):
            return f"跳过已存在: {dst_path}"
        
        try:
            shutil.copy2(src_path, dst_path)
            return f"复制成功: {src_path} -> {dst_path}"
        except Exception as e:
            return f"复制失败: {src_path}, 错误: {str(e)}"
    
    else:
        return f"跳过不支持的格式: {src_path}"

def convert_wav_to_mp3(src_root, dst_root, max_workers=None):
    """
    使用多进程递归遍历 src_root 下的所有音频文件，
    WAV 文件转换为 MP3，MP3 文件直接复制，
    保存在 dst_root 下，保持目录结构和文件名一致。
    若目标文件已存在则跳过。
    """
    if max_workers is None:
        max_workers = cpu_count()
    
    # 收集所有需要处理的文件
    file_list = []
    total_files = 0
    wav_files = 0
    mp3_files = 0
    
    for root, dirs, files in os.walk(src_root):
        for file in files:
            total_files += 1
            file_ext = os.path.splitext(file)[1].lower()
            
            if file_ext == ".wav":
                wav_files += 1
                file_list.append((root, file))
            elif file_ext == ".mp3":
                mp3_files += 1
                file_list.append((root, file))
    
    print(f"扫描完成: 总文件 {total_files} 个，WAV文件 {wav_files} 个，MP3文件 {mp3_files} 个")
    print(f"准备处理 {len(file_list)} 个音频文件，使用 {max_workers} 个进程")
    
    if not file_list:
        print("没有找到需要处理的音频文件")
        return
    
    # 准备传递给多进程的参数
    args_list = [((root, file), src_root, dst_root) for root, file in file_list]
    
    # 使用多进程处理文件
    with Pool(processes=max_workers) as pool:
        results = pool.map(process_single_file, args_list)
    
    # 统计结果
    success_count = 0
    skip_count = 0
    error_count = 0
    
    for result in results:
        print(result)
        if "成功" in result:
            success_count += 1
        elif "跳过" in result:
            skip_count += 1
        else:
            error_count += 1
    
    print(f"\n处理完成: 成功 {success_count} 个，跳过 {skip_count} 个，失败 {error_count} 个")

if __name__ == "__main__":
    # 源文件夹路径（包含音频文件）
    source_folder = "/Users/zhanjun/Documents/papers/VoiceGenEval/VoiceGenEval.github.io/data/examples_old"
    # 目标文件夹路径（用于保存 mp3 文件）
    target_folder = "/Users/zhanjun/Documents/papers/VoiceGenEval/VoiceGenEval.github.io/data/examples"
    
    # 可以指定进程数，不指定则使用 CPU 核心数
    convert_wav_to_mp3(source_folder, target_folder, max_workers=4)