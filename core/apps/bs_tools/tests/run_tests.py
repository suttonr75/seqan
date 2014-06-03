#!/usr/bin/env python
"""Execute the tests for bs_tools.

The golden test outputs are generated by the script generate_outputs.sh.

You have to give the root paths to the source and the binaries as arguments to
the program.  These are the paths to the directory that contains the 'projects'
directory.

Usage:  run_tests.py SOURCE_ROOT_PATH BINARY_ROOT_PATH
"""
import logging
import os.path
import sys

# Automagically add util/py_lib to PYTHONPATH environment variable.
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..',
                                    '..', '..', 'util', 'py_lib'))
sys.path.insert(0, path)

import seqan.app_tests as app_tests

def main(source_base, binary_base):
    """Main entry point of the script."""

    print 'Executing test for bs_tools'
    print '========================='
    print
   
    ##############################################################
    ### Casbar
    ##############################################################
    ph = app_tests.TestPathHelper(
        source_base, binary_base,
        'core/apps/bs_tools/tests')  # tests dir

    # ============================================================
    # Auto-detect the binary path.
    # ============================================================

    path_to_bisar = app_tests.autolocateBinary(
      binary_base, 'core/apps/bs_tools', 'bisar')
    path_to_casbar = app_tests.autolocateBinary(
      binary_base, 'core/apps/bs_tools', 'casbar')

    # ============================================================
    # Built TestConf list.
    # ============================================================

    # Build list with TestConf objects, analoguely to how the output
    # was generated in generate_outputs.sh.
    conf_list = []

    # ============================================================
    # se
    # ============================================================

    # App TestConf objects to conf_list, just like this for each
    # test you want to run.
    # 0
    conf = app_tests.TestConf(
        program=path_to_bisar,
        redir_stdout=ph.outFile('other.stdout'),
        args=['-e3', str(4), '-e4', str(5),    
              #-e3 4 -e4 5
              '-o', ph.outFile('reads_se_N6000_0.CT_GA.verified.sam'),
              ph.inFile('reads_se_N6000.CT_GA.sam'),
              ph.inFile('hg18_chr21_3000.fa'),
              ph.inFile('reads_se_N6000.fastq')],
        to_diff=[#(ph.inFile('STDOUT_FILE'),
                  #ph.outFile('STDOUT_FILE')),
                 (ph.inFile('reads_se_N6000_0.CT_GA.verified.sam'),
                  ph.outFile('reads_se_N6000_0.CT_GA.verified.sam'))])
    conf_list.append(conf)
    # 1
    conf = app_tests.TestConf(
        program=path_to_bisar,
        redir_stdout=ph.outFile('other.stdout'),
        args=['-gas', str(-4.5), '-ges', str(-2.0), '-der', str(0.001), '-bsc', str(0.99), '-gmr', str(0.5), '-i', str(0.8), '-rn', str(0.001), '-pms', str(0.9), '-mq', str(0), '-e3', str(4), '-e4', str(5),   
              # -gas -4.5 -ges -2.0 -der 0.001 -bsc 0.99 -gmr 0.5 -i 0.8 -rn 0.001 -pms 0.9 -mq 0 -e3 4 -e4 5
              '-o', ph.outFile('reads_se_N6000_1.CT_GA.verified.sam'),
              ph.inFile('reads_se_N6000.CT_GA.sam'),
              ph.inFile('hg18_chr21_3000.fa'),
              ph.inFile('reads_se_N6000.fastq')],
        to_diff=[#(ph.inFile('STDOUT_FILE'),
                  #ph.outFile('STDOUT_FILE')),
                 (ph.inFile('reads_se_N6000_1.CT_GA.verified.sam'),
                  ph.outFile('reads_se_N6000_1.CT_GA.verified.sam'))])
    conf_list.append(conf)

    # 2
    conf = app_tests.TestConf(
        program=path_to_bisar,
        redir_stdout=ph.outFile('other.stdout'),
        args=['-nse', '-nsi', '-nsd', '-gas', str(-4.5), '-ges', str(-2.0), '-der', str(0.001), '-bsc', str(0.99), '-gmr', str(0.5), '-i', str(0.8), '-rn', str(0.001), '-pms', str(0.9), '-mq', str(0), '-e3', str(4), '-e4', str(5),   
              # -nse -nsi -nsd -gas -4.5 -ges -2.0 -der 0.001 -bsc 0.99 -gmr 0.5 -i 0.8 -rn 0.001 -pms 0.9 -mq 0 -e3 4 -e4 5 
              '-o', ph.outFile('reads_se_N6000_2.CT_GA.verified.sam'),
              ph.inFile('reads_se_N6000.CT_GA.sam'),
              ph.inFile('hg18_chr21_3000.fa'),
              ph.inFile('reads_se_N6000.fastq')],
        to_diff=[(ph.inFile('reads_se_N6000_2.CT_GA.verified.sam'),
                  ph.outFile('reads_se_N6000_2.CT_GA.verified.sam'))])
    conf_list.append(conf)

    # 3
    conf = app_tests.TestConf(
        program=path_to_bisar,
        redir_stdout=ph.outFile('other.stdout'),
        args=['-nse', '-nsi', '-nsd', '-gas', str(-4.5), '-ges', str(-2.0), '-der', str(0.001), '-bsc', str(0.99), '-gmr', str(0.2), '-i', str(0.8), '-rn', str(0.001), '-pms', str(0.9), '-mq', str(0), '-e3', str(4), '-e4', str(5),   
              # -nse -nsi -nsd -gas -4.5 -ges -2.0 -der 0.001 -bsc 0.99 -gmr 0.2 -i 0.8 -rn 0.001 -pms 0.9 -mq 0 -e3 4 -e4 5
              '-o', ph.outFile('reads_se_N6000_3.CT_GA.verified.sam'),
              ph.inFile('reads_se_N6000.CT_GA.sam'),
              ph.inFile('hg18_chr21_3000.fa'),
              ph.inFile('reads_se_N6000.fastq')],
        to_diff=[(ph.inFile('reads_se_N6000_3.CT_GA.verified.sam'),
                  ph.outFile('reads_se_N6000_3.CT_GA.verified.sam'))])
    conf_list.append(conf)

    # 4
    conf = app_tests.TestConf(
        program=path_to_bisar,
        redir_stdout=ph.outFile('other.stdout'),
        args=['-nse', '-nsi', '-nsd', '-gas', str(-4.5), '-ges', str(-2.0), '-der', str(0.001), '-bsc', str(0.99), '-gmr', str(0.8), '-i', str(0.8), '-rn', str(0.001), '-pms', str(0.9), '-mq', str(0), '-e3', str(4), '-e4', str(5),   
              # -nse -nsi -nsd -gas -4.5 -ges -2.0 -der 0.001 -bsc 0.99 -gmr 0.8 -i 0.8 -rn 0.001 -pms 0.9 -mq 0 -e3 4 -e4 5
              '-o', ph.outFile('reads_se_N6000_4.CT_GA.verified.sam'),
              ph.inFile('reads_se_N6000.CT_GA.sam'),
              ph.inFile('hg18_chr21_3000.fa'),
              ph.inFile('reads_se_N6000.fastq')],
        to_diff=[(ph.inFile('reads_se_N6000_4.CT_GA.verified.sam'),
                  ph.outFile('reads_se_N6000_4.CT_GA.verified.sam'))])
    conf_list.append(conf)


    # ============================================================
    # pe
    # ============================================================
    # 0
    conf = app_tests.TestConf(
        program=path_to_bisar,
        redir_stdout=ph.outFile('other.stdout'),
        args=['-e3', str(4), '-e4', str(5),    
              #-e3 4 -e4 5
              '-o', ph.outFile('reads_pe_N6000_0.CT_GA.verified.sam'),
              ph.inFile('reads_pe_N6000.CT_GA.sam'),
              ph.inFile('hg18_chr21_3000.fa'),
              ph.inFile('reads_pe_N6000.L.fastq'),
              ph.inFile('reads_pe_N6000.R.fastq')],
        to_diff=[(ph.inFile('reads_pe_N6000_0.CT_GA.verified.sam'),
                  ph.outFile('reads_pe_N6000_0.CT_GA.verified.sam'))])
    conf_list.append(conf)


    ##############################################################
    ### Casbar
    ##############################################################

    # 0
    conf = app_tests.TestConf(
        program=path_to_casbar,
        redir_stdout=ph.outFile('other.stdout'),
        args=['-nec', '-umq', '-mc', str(6), '-msc', str(5), '-mpc', str(0.5), '-hes', str(0.005),
              '-o', ph.outFile('snps_se_0.vcf'),
              '-b', ph.outFile('meths_se_0.bed'),
              ph.inFile('hg18_chr21_3000.fa'),
              ph.inFile('reads_se_N6000_2.CT_GA.verified.pos_so.sam')],
        to_diff=[(ph.inFile('snps_se_0.vcf'),
                  ph.outFile('snps_se_0.vcf')),
                  (ph.inFile('meths_se_0.bed'),
                  ph.outFile('meths_se_0.bed'))])
    conf_list.append(conf)
   
    # ============================================================
    # pe
    # ============================================================
    # 0
    conf = app_tests.TestConf(
        program=path_to_casbar,
        redir_stdout=ph.outFile('other.stdout'),
        args=['-nec', '-umq', '-mc', str(6), '-msc', str(5), '-mpc', str(0.5), '-hes', str(0.005),
              '-o', ph.outFile('snps_pe_0.vcf'),
              '-b', ph.outFile('meths_pe_0.bed'),
              ph.inFile('hg18_chr21_3000.fa'),
              ph.inFile('reads_pe_N6000_0.CT_GA.verified.pos_so.sam')],
        to_diff=[(ph.inFile('snps_pe_0.vcf'),
                  ph.outFile('snps_pe_0.vcf')),
                  (ph.inFile('meths_pe_0.bed'),
                  ph.outFile('meths_pe_0.bed'))])
    conf_list.append(conf)

    # ============================================================
    # Execute the tests.
    # ============================================================
    failures = 0
    for conf in conf_list:
        res = app_tests.runTest(conf)
        # Output to the user.
        print ' '.join([os.path.basename(conf.program)] + conf.args),
        if res:
             print 'OK'
        else:
            failures += 1
            print 'FAILED'

    # Cleanup.
    ph.deleteTempDir()

    print '=============================='
    print '     total tests: %d' % len(conf_list)
    print '    failed tests: %d' % failures
    print 'successful tests: %d' % (len(conf_list) - failures)
    print '=============================='


    # Compute and return return code.
    return failures != 0


if __name__ == '__main__':
    sys.exit(app_tests.main(main))
