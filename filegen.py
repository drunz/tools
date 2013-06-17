import sys, uuid, os

def gen_files(folder, size_mb, num_files):
	for i in xrange(num_files):
		fid = str(uuid.uuid4())
		filename = os.path.join(folder, fid)

		with open(filename, 'w+') as f:
			for i in xrange(size_mb):
				f.write(os.urandom(1024**2))

def main(args):
	num_folders = int(args[1]) if len(args) > 1 else 10
	num_files   = int(args[2]) if len(args) > 2 else 1  # per folder
	target      =     args[3]  if len(args) > 3 else 'out'
	size        = int(args[4]) if len(args) > 4 else 10

	print '============================================================'
	print 'Generating %d folders with %d files of size %d MB...' % (num_folders, num_files, size)
	print 'Target folder:', target
	print 'Usage: filegen.py [num_folders] [num_files] [target_folder] [file_size (MB)]'
	print '============================================================'

	# generate folders and files
	for i in xrange(num_folders):
		fid = str(uuid.uuid4())
		folder = os.path.join(target, fid)
		os.makedirs(folder)
		
		print '[%d/%d]' % (i+1, num_folders), folder, '->', num_files, '*', size, 'MB'
		gen_files(folder, size, num_files)
		

if __name__ == "__main__":
	main(sys.argv)
